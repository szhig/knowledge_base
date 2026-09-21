from fastapi import APIRouter

from app.dependencies import DBSession, CurrentUser

router = APIRouter()


@router.get("/")
async def list_tags(db: DBSession, user: CurrentUser):
    ...


@router.post("/")
async def create_tag(db: DBSession, user: CurrentUser):
    ...


@router.put("/{tag_id}")
async def update_tag(tag_id: int, db: DBSession, user: CurrentUser):
    ...


@router.delete("/{tag_id}")
async def delete_tag(tag_id: int, db: DBSession, user: CurrentUser):
    ...
