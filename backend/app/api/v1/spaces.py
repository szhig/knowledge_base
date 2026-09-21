from fastapi import APIRouter

from app.dependencies import DBSession, CurrentUser

router = APIRouter()


@router.get("/")
async def list_spaces(db: DBSession, user: CurrentUser):
    ...


@router.post("/")
async def create_space(db: DBSession, user: CurrentUser):
    ...


@router.get("/{space_id}")
async def get_space(space_id: int, db: DBSession, user: CurrentUser):
    ...


@router.put("/{space_id}")
async def update_space(space_id: int, db: DBSession, user: CurrentUser):
    ...


@router.post("/{space_id}/members")
async def add_member(space_id: int, db: DBSession, user: CurrentUser):
    ...


@router.put("/{space_id}/members/{user_id}")
async def update_member(space_id: int, user_id: int, db: DBSession, user: CurrentUser):
    ...


@router.delete("/{space_id}/members/{user_id}")
async def remove_member(space_id: int, user_id: int, db: DBSession, user: CurrentUser):
    ...
