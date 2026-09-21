from fastapi import APIRouter, Query

from app.dependencies import DBSession, CurrentUser

router = APIRouter()


@router.get("/")
async def search(q: str = Query(...), db: DBSession = None, user: CurrentUser = None):
    ...


@router.get("/suggest")
async def suggest(q: str = Query(...), db: DBSession = None, user: CurrentUser = None):
    ...


@router.get("/semantic")
async def semantic_search(q: str = Query(...), db: DBSession = None, user: CurrentUser = None):
    ...
