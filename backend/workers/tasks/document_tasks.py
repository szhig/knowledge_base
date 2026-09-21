from workers.celery_app import celery_app


@celery_app.task(name="parse_document")
def parse_document(document_id: int) -> None:
    """Parse uploaded document: extract text → chunk → index."""
    # TODO: implement document parsing pipeline
    # 1. Fetch document from DB
    # 2. Download file from MinIO
    # 3. Extract text (PyMuPDF / python-docx / etc.)
    # 4. Update document.content_text + status
    # 5. Chunk text → document_chunks
    # 6. Trigger embedding task for each chunk
    pass
