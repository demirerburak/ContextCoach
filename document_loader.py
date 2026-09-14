import json

from models import Document, KnowledgeBase


def load_document(path: str) -> Document:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return Document.model_validate(data)


def load_knowledge_base(path: str) -> KnowledgeBase:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return KnowledgeBase.model_validate(data)


if __name__ == "__main__":
    document = load_document("document.json")
    print(document.model_dump(mode="json"))
    knowledge_base = load_knowledge_base("knowledge_base.json")
    print(
    knowledge_base.model_dump_json(
        indent=2,
        exclude_none=True,
    )
)
