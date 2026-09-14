from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class EvaluationTaskType(str, Enum):
    QUESTION_ANSWERING = "question_answering"
    SUMMARY = "summary"
    COMPARISON = "comparison"
    RECOMMENDATION = "recommendation"
    ABSTENTION = "abstention"


class EvaluationCase(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    case_id: str = Field(min_length=1)
    task_type: EvaluationTaskType
    question: str = Field(min_length=1)
    target_collection_ids: list[str] = Field(min_length=1)
    expected_terms: list[str] = Field(default_factory=list)
    should_abstain: bool = False


class EvaluationSuite(BaseModel):
    model_config = ConfigDict(extra="forbid")

    cases: list[EvaluationCase] = Field(min_length=1)