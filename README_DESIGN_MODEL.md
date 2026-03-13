# Resume vs Job Description - Minimal Backend Model

Minimal backend structure for comparing a resume against a job description and returning a structured evaluation.

## Project Structure

```text
app.py

models/
  evaluation_request.py
  evaluation_result.py

services/
  evaluator.py
  llm_client.py

data/
  sample_data.py
```

## 3) Simple Relationships

1. `Evaluator` service takes one `EvaluationRequest` and returns one `EvaluationResult`.
2. Conceptually this is a `1 -> 1` request-to-result relationship per evaluation call.
3. `EvaluationRequest.job_id` resolves to one job record in `JOB_DESCRIPTIONS`.

## Minimal JSON Shapes

### Input

```json
{
  "resume_id": "resume_042",
  "job_id": "api_engineer_001",
  "resume_text": "Software engineer with 4 years in Python, Flask APIs, PostgreSQL, and AWS. Built CI/CD pipelines."
}
```

### Output

```json
{
  "resume_id": "resume_042",
  "match_score": 8,
  "strengths": [
    "Shows evidence of python.",
    "Shows evidence of rest.",
    "Shows evidence of sql."
  ],
  "gaps": [
    "No clear evidence of cloud.",
    "Could provide more measurable impact and project details.",
    "Could better highlight ownership and scope of work."
  ],
  "recommendation": "Interview"
}
```

## Notes on Implementation

- `data/sample_data.py` provides multiple hardcoded jobs (`JOB_DESCRIPTIONS`) and multiple sample requests (`SAMPLE_REQUESTS`).
- `services/evaluator.py` has two methods:
  - `evaluate(...)`: original raw keyword-based scoring.
  - `evaluate_with_llm(...)`: OpenAI-based scoring with fallback to `evaluate(...)` on failure.
- `services/llm_client.py` handles OpenAI calls and validates the JSON response shape.
- `resume_id` is passed through request -> result so each output is traceable to a specific resume.
- `services/evaluator.py` uses `_fill_unique(...)` so strengths and gaps remain unique while still meeting the 3-item requirement. (this is only for the non-LLM fallback, the llm evaluate method doesn't use this)
- `models/evaluation_result.py` enforces validation for score bounds, list sizes, and recommendation values.

## Keywords Used In Raw Fallback Evaluator

Used only by `evaluate(...)` (manual keyword-based fallback), not by `evaluate_with_llm(...)`.

`python`, `rest`, `api`, `sql`, `aws`, `cloud`, `docker`, `kubernetes`, `flask`, `fastapi`, `django`, `postgresql`, `redis`, `microservices`, `ci/cd`, `terraform`, `airflow`, `etl`, `monitoring`, `incident`
