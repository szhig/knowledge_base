from workers.celery_app import celery_app


@celery_app.task(name="index_note")
def index_note(note_id: int) -> None:
    """Sync a single note to Elasticsearch notes_index."""
    # TODO: fetch note from DB → build ES doc → index to ES
    pass


@celery_app.task(name="reindex_all_notes")
def reindex_all_notes(user_id: int | None = None) -> None:
    """Rebuild the entire notes_index from MySQL."""
    # TODO: batch fetch all notes → bulk index to ES
    pass


@celery_app.task(name="delete_note_from_index")
def delete_note_from_index(note_id: int) -> None:
    """Remove a note from Elasticsearch index."""
    # TODO: delete by note_id from ES
    pass
