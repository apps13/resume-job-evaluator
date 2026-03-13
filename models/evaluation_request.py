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
