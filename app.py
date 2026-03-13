import json
from dataclasses import asdict

from data.sample_data import SAMPLE_REQUESTS
from services.evaluator import Evaluator


def main() -> None:
    evaluator = Evaluator()

    for request in SAMPLE_REQUESTS:
        print(f"\nEvaluation for job_id: {request.job_id}")
        result = evaluator.evaluate_with_llm(request)
        print(json.dumps(asdict(result), indent=2))
    
    # Or if I want to just return for a single request
    # request = SAMPLE_REQUESTS[3]
    # result = evaluator.evaluate_with_llm(request)
    # print(json.dumps(asdict(result), indent=2))


if __name__ == "__main__":
    main()
