from dataclasses import dataclass


@dataclass(frozen=True)
class EvaluationRequest:
    """Input data for evaluating a job application."""

    # initially had this
    # job_description = str

    # to make it more understandable, switched to job_id that maps to a job description
    resume_id: str
    job_id: str
    resume_text: str

    def validate(self) -> None:
        if not isinstance(self.resume_id, str) or not self.resume_id.strip():
            raise ValueError("resume_id must be a non-empty string")
        if not isinstance(self.job_id, str) or not self.job_id.strip():
            raise ValueError("job_id must be a non-empty string")
        if not isinstance(self.resume_text, str) or not self.resume_text.strip():
            raise ValueError("resume_text must be a non-empty string")
