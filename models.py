from datetime import date
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class DocumentType(str, Enum):
    REFERENCE = "reference"
    PERSONAL_NOTE = "personal_note"


class Collection(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    collection_id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    description: str | None = None


class Document(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    document_id: str = Field(min_length=1)
    collection_id: str = Field(min_length=1)
    document_type: DocumentType
    title: str = Field(min_length=1)
    text: str = Field(min_length=1)
    source_url: HttpUrl | None = None
    source_date: date | None = None


class KnowledgeBase(BaseModel):
    model_config = ConfigDict(extra="forbid")

    collections: list[Collection] = Field(min_length=1)
    documents: list[Document] = Field(min_length=1)


