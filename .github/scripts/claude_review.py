"""
Claude AI Code Review Script
Called by .github/workflows/ai-review.yml on every Pull Request.
Posts a detailed code review as a PR comment.
"""
import anthropic
import os
import requests
import sys


def review_code_with_claude(diff: str) -> str:
    """Send diff to Claude and return a markdown review."""
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    prompt = f"""You are an expert code reviewer with deep Python knowledge. Review the following git diff and provide a concise, actionable review.

Structure your review as:

## Summary
One sentence describing what changed.

## Potential Issues
Any bugs, edge cases, or logic errors. If none, say "None found."

## Code Quality
Readability, naming, structure, type hints, docstrings.

## Security
Any security concerns. If none, say "No security issues."

## Suggestions
Up to 3 specific, actionable improvements with short code examples where helpful.

Be concise. Use markdown. Focus on what matters most.

```diff
{diff}
```"""

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text


def post_pr_comment(review: str):
    """Post the review as a GitHub PR comment."""
    token = os.environ.get("GITHUB_TOKEN")
    pr_number = os.environ.get("PR_NUMBER")
    repo = os.environ.get("REPO_FULL_NAME")

    if not all([token, pr_number, repo]):
        print("Missing GitHub env vars — printing review to stdout:")
        print(review)
        return

    comment_body = f"""## 🤖 AI Code Review

{review}

---
*Automated review by Claude AI. This is a suggestion — human review is still required before merging.*
"""

    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.post(url, json={"body": comment_body}, headers=headers)

    if response.status_code == 201:
        print("✅ Review posted successfully to PR!")
    else:
        print(f"❌ Failed to post comment: {response.status_code} {response.text}")
        print("--- Review ---")
        print(review)


if __name__ == "__main__":
    diff_file = "/tmp/pr_diff.txt"

    try:
        with open(diff_file) as f:
            diff = f.read()
    except FileNotFoundError:
        print("No diff file found — skipping review.")
        sys.exit(0)

    if not diff.strip():
        print("Empty diff — skipping review.")
        sys.exit(0)

    # Trim very large diffs to stay within token limits
    if len(diff) > 8000:
        diff = diff[:8000] + "\n\n... [diff truncated — showing first 8000 chars]"

    print("🔍 Sending diff to Claude for review...")
    review = review_code_with_claude(diff)
    post_pr_comment(review)
