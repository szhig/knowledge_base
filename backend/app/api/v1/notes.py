from fastapi import APIRouter

from app.dependencies import DBSession, CurrentUser

router = APIRouter()


@router.get("/")
async def list_notes(db: DBSession, user: CurrentUser):
    ...


@router.post("/")
async def create_note(db: DBSession, user: CurrentUser):
    ...


@router.get("/{note_id}")
async def get_note(note_id: int, db: DBSession, user: CurrentUser):
    ...


@router.put("/{note_id}")
async def update_note(note_id: int, db: DBSession, user: CurrentUser):
    ...


@router.delete("/{note_id}")
async def delete_note(note_id: int, db: DBSession, user: CurrentUser):
    ...


@router.get("/{note_id}/backlinks")
async def get_backlinks(note_id: int, db: DBSession, user: CurrentUser):
    ...


@router.get("/{note_id}/versions")
async def get_versions(note_id: int, db: DBSession, user: CurrentUser):
    ...


@router.get("/{note_id}/graph")
async def get_note_graph(note_id: int, db: DBSession, user: CurrentUser):
    ...
