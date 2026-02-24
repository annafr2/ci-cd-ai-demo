# CI/CD + AI Demo 🚀

Demo repository for the guest lecture: **"From Manual Development to AI-Assisted Pipeline"**

**Course:** Software Project Management (4080015) | SCE Beer Sheva | 2025-26

---

## 📁 What's in this repo

| File | Purpose |
|------|---------|
| `shipping.py` | Main code — shipping cost calculator ✅ |
| `shipping_broken.py` | Intentionally broken version (for the break demo) ❌ |
| `tests/test_shipping.py` | Unit tests — 13 test cases (pytest) |
| `.github/workflows/ci.yml` | CI pipeline — runs tests on every push |
| `.github/workflows/ai-review.yml` | AI code review on every PR |
| `.github/scripts/claude_review.py` | Claude API review script |

---

## 🎯 Try it yourself!

1. **Fork** this repo (button at top right)
2. Click on any file → click the ✏️ pencil icon to edit
3. Make any small change and click **Commit changes**
4. Go to the **Actions** tab → watch your pipeline run!

---

## 🔑 Setting up AI Code Review (optional)

1. Get a free API key from [console.anthropic.com](https://console.anthropic.com)
2. In your forked repo: **Settings → Secrets and variables → Actions**
3. Click **"New repository secret"**
4. Name: `ANTHROPIC_API_KEY` | Value: your key
5. Open a Pull Request → Claude reviews it automatically 🤖

---

## 💻 Run locally

```bash
pip install pytest
pytest tests/ -v
```
