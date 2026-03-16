from models.evaluation_request import EvaluationRequest
from models.evaluation_result import EvaluationResult
from data.sample_data import JOB_DESCRIPTIONS
from services.llm_client import LLMClient


class Evaluator:
    """Compares resume text to job description text."""

    KEYWORDS = [
        "python",
        "rest",
        "api",
        "sql",
        "aws",
        "cloud",
        "docker",
        "kubernetes",
        "flask",
        "fastapi",
        "django",
        "postgresql",
        "redis",
        "microservices",
        "ci/cd",
        "terraform",
        "airflow",
        "etl",
        "monitoring",
        "incident",
    ]

    @staticmethod
    def _fill_unique(existing: list[str], fallback: list[str], size: int = 3) -> list[str]:
        result: list[str] = []

        for item in existing:
            if item not in result:
                result.append(item)
            if len(result) == size:
                return result

        for item in fallback:
            if item not in result:
                result.append(item)
            if len(result) == size:
                return result

        return result

    def evaluate(self, request: EvaluationRequest) -> EvaluationResult:
        """Original keyword-based evaluator."""
        request.validate()

        job = None
        for item in JOB_DESCRIPTIONS:
            if item["job_id"] == request.job_id:
                job = item
                break

        if job is None:
            print(
                f"Job ID '{request.job_id}' was not found. Returning a default evaluation."
            )
            result = EvaluationResult(
                resume_id=request.resume_id,
                match_score=1,
                strengths=[
                    "Resume content was received successfully.",
                    "Evaluation pipeline is available.",
                    "Request format is valid.",
                ],
                gaps=[
                    "Selected job_id does not match any known job description.",
                    "Please use a valid job_id from the data layer.",
                    "Re-run evaluation with a matching job posting.",
                ],
                recommendation="No",
            )
            result.validate()
            return result

        jd = job["job_description"].lower() # setting to job description of the found job
        resume = request.resume_text.lower()

        required_keywords = [word for word in self.KEYWORDS if word in jd]

        matched = [word for word in required_keywords if word in resume]
        missing = [word for word in required_keywords if word not in resume]

        # Keep scoring simple and bounded to the required 1..10 range.
        base_score = 2 + (2 * len(matched)) - len(missing) # base score of 2 and +2 if matched, -1 if missing
        match_score = max(1, min(10, base_score))

        strengths = self._fill_unique(
            existing=[f"Shows evidence of {word}." for word in matched],
            fallback=[
                "Resume demonstrates generally relevant engineering experience.",
                "Background indicates practical delivery of backend features.",
                "Experience appears aligned with core role expectations.",
            ],
        )

        gaps = self._fill_unique(
            existing=[f"No clear evidence of {word}." for word in missing],
            fallback=[
                "Could provide more measurable impact and project details.",
                "Could better highlight ownership and scope of work.",
                "Could include stronger evidence of production-scale outcomes.",
            ],
        )

        if match_score >= 8:
            recommendation = "Interview"
        elif match_score >= 5:
            recommendation = "Maybe"
        else:
            recommendation = "No"

        result = EvaluationResult(
            resume_id=request.resume_id,
            match_score=match_score,
            strengths=strengths,
            gaps=gaps,
            recommendation=recommendation,
        )
        result.validate()
        return result

    def evaluate_with_llm(self, request: EvaluationRequest) -> EvaluationResult:
        """LLM-based evaluator with fallback to the original keyword logic."""
        request.validate()

        job = None
        for item in JOB_DESCRIPTIONS:
            if item["job_id"] == request.job_id:
                job = item
                break

        if job is None:
            return self.evaluate(request) # will print out the neat error message defined in above evaluate function

        try:
            # Call evaluate function in LLMClient class
            llm_data = LLMClient().evaluate(
                job_description=job["job_description"],
                resume_text=request.resume_text,
            )
            result = EvaluationResult(
                resume_id=request.resume_id,
                match_score=llm_data["match_score"],
                strengths=llm_data["strengths"],
                gaps=llm_data["gaps"],
                recommendation=llm_data["recommendation"],
            )
            result.validate()
            return result
        except Exception as exc:
            # If LLM evaluation fails, fall back to keyword-based evaluation
            print(f"LLM evaluation failed, falling back to keyword mode: {exc}")
            return self.evaluate(request)
