# Resume Matcher

This project evaluates how well a resume matches a job description and returns a score, strengths, gaps, and a recommendation.

## Quick Start

1. Install dependencies:

```bash
pip install openai python-dotenv
```

2. Create a local `.env` file (never commit this file):

```env
OPENAI_API_KEY=your_openai_key_here
OPENAI_MODEL=gpt-4o-mini
```

You can copy from `.env.example` and fill in your values.

3. Run the app:

```bash
python app.py
```

Notes:
- If the LLM call fails, evaluation automatically falls back to the original raw keyword evaluator.
- `app.py` uses `Evaluator.evaluate_with_llm(...)` by default.
- Your OpenAI key is read from your local `.env` file.

For project structure and design details, see `README_DESIGN_MODEL.md`.
