from dataclasses import dataclass
from typing import Literal


Recommendation = Literal["Interview", "Maybe", "No"]


@dataclass(frozen=True)
class EvaluationResult:
    """Output data from evaluating a job application."""

    resume_id: str
    match_score: int
    strengths: list[str]
    gaps: list[str]
    recommendation: Recommendation

    def validate(self) -> None:
        if not 1 <= self.match_score <= 10:
            raise ValueError("match_score must be between 1 and 10")
        if len(self.strengths) != 3:
            raise ValueError("strengths must contain exactly 3 items")
        if len(self.gaps) != 3:
            raise ValueError("gaps must contain exactly 3 items")
        if self.recommendation not in {"Interview", "Maybe", "No"}:
            raise ValueError("recommendation must be Interview, Maybe, or No")
