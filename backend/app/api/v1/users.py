from fastapi import APIRouter

from app.dependencies import DBSession, CurrentUser

router = APIRouter()


@router.get("/")
async def list_users(db: DBSession, user: CurrentUser):
    ...


@router.put("/{user_id}")
async def update_user(user_id: int, db: DBSession, user: CurrentUser):
    ...
