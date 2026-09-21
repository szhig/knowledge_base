from workers.celery_app import celery_app


@celery_app.task(name="generate_embedding")
def generate_embedding(text: str) -> list[float]:
    """Generate embedding vector for given text."""
    # TODO: call embedding API (OpenAI text-embedding-3-small)
    pass


@celery_app.task(name="embed_document_chunks")
def embed_document_chunks(document_id: int) -> None:
    """Generate embeddings for all chunks of a document and index to ES."""
    # TODO: fetch chunks → embed each → index to ES documents_index
    pass
