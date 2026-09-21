from fastapi import APIRouter, Query

from app.dependencies import DBSession, CurrentUser

router = APIRouter()


@router.get("/")
async def get_graph(
    space_id: int | None = Query(default=None),
    depth: int = Query(default=2, ge=1, le=5),
    db: DBSession = None,
    user: CurrentUser = None,
):
    ...


@router.get("/note/{note_id}")
async def get_note_graph(
    note_id: int,
    depth: int = Query(default=2, ge=1, le=5),
    db: DBSession = None,
    user: CurrentUser = None,
):
    ...
