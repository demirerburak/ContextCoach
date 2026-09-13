import json


def load_document(path: str) -> dict:
    # 1. Dosyayı UTF-8 olarak aç.
    with open(path, "r", encoding="utf-8") as file:
    # 2. json.load(...) ile Python sözlüğüne dönüştür.
        document = json.load(file)
    if not isinstance(document, dict):
        raise ValueError("Document JSON must be an object.")
    # 3. "text" alanını kontrol et.
    document_text = document.get("text")
    # 4. Alan yoksa, metin değilse veya boşsa ValueError oluştur.
    if not isinstance(document_text, str) or not document_text.strip():
        raise ValueError("Document must contain a non-empty 'text' field.")
    return document


if __name__ == "__main__":
    document = load_document("document.json")
    print(document)