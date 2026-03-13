import json
import os
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv() # look for a .env file and load values into environment


class LLMClient:
    """Minimal OpenAI wrapper for resume-to-job evaluation."""

    def __init__(self) -> None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set")
        
        # initializes the OpenAI client
        # using environment variables so the API key is not hardcoded in source code
        self._client = OpenAI(api_key=api_key)
        self._model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    @staticmethod
    def _extract_json(text: str) -> dict[str, Any]:
        start = text.find("{")
        end = text.rfind("}")
        if start == -1 or end == -1 or end <= start:
            raise ValueError("No JSON object found in LLM response")
        
        # Take the json output and make it a python dict to easily work with
        payload = json.loads(text[start : end + 1])
        if not isinstance(payload, dict):
            raise ValueError("LLM response is not a JSON object")
        return payload

    @staticmethod
    def _validate(payload: dict[str, Any]) -> dict[str, Any]:
        match_score = payload.get("match_score")
        strengths = payload.get("strengths")
        gaps = payload.get("gaps")

        # Checking if our result adheres to the expected schema
        if payload.get("recommendation") not in {"Interview", "Maybe", "No"}:
            raise ValueError("recommendation must be Interview, Maybe, or No")
        if not isinstance(match_score, int) or not 1 <= match_score <= 10:
            raise ValueError("match_score must be an int between 1 and 10")
        if not isinstance(strengths, list) or len(strengths) != 3 or not all(isinstance(i, str) for i in strengths):
            raise ValueError("strengths must be a list of 3 strings")
        if not isinstance(gaps, list) or len(gaps) != 3 or not all(isinstance(i, str) for i in gaps):
            raise ValueError("gaps must be a list of 3 strings")

        return {
            "match_score": match_score,
            "strengths": strengths,
            "gaps": gaps,
            "recommendation": payload["recommendation"],
        }

    # This method will be called in the evaluator class by evaluate_with_llm
    def evaluate(self, job_description: str, resume_text: str) -> dict[str, Any]:
        prompt = (
            "Evaluate resume fit to job description. Return only valid JSON with this exact schema: "
            '{"match_score": int 1-10, "strengths": [3 strings], "gaps": [3 strings], '
            '"recommendation": "Interview"|"Maybe"|"No"}. '
            "Base output only on provided text."
        )

        response = self._client.chat.completions.create(
            model=self._model,
            temperature=0, # the less the temp, the more deterministic the output
            messages=[ # message we send to model
                {"role": "system", "content": prompt},
                {
                    "role": "user",
                    "content": (
                        "Job Description:\n"
                        f"{job_description}\n\n"
                        "Resume:\n"
                        f"{resume_text}"
                    ),
                },
            ],
        )

        text = response.choices[0].message.content or ""
        return self._validate(self._extract_json(text))
