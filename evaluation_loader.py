import json

from evaluation_models import EvaluationSuite


def load_evaluation_suite(path: str) -> EvaluationSuite:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return EvaluationSuite.model_validate(data)


if __name__ == "__main__":
    suite = load_evaluation_suite("evaluation_cases.json")

    print(f"Toplam vaka: {len(suite.cases)}")

    for case in suite.cases:
        print(
            case.case_id,
            case.task_type.value,
            case.should_abstain,
        )