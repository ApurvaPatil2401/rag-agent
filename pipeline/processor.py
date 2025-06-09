# pipeline/processor.py

def process_documents(raw_docs):
    cleaned = []

    for doc in raw_docs:
        cleaned.append({
            "title": doc.get("title", ""),
            "doc_type": doc.get("document_type", ""),
            "publication_date": doc.get("publication_date", "")[:10],
            "president": doc.get("president", "Unknown"),
            "summary": (doc.get("abstract") or "")[:500],  # ✅ Fix applied here
        })

    return cleaned
