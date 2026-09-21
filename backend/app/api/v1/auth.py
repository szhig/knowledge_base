from fastapi import APIRouter

from app.dependencies import DBSession, CurrentUser
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse, UserResponse

router = APIRouter()


@router.post("/register", response_model=UserResponse)
async def register(req: RegisterRequest, db: DBSession):
    ...


@router.post("/login", response_model=TokenResponse)
async def login(req: LoginRequest, db: DBSession):
    ...


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(refresh_token: str, db: DBSession):
    ...


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: CurrentUser):
    return UserResponse.model_validate(current_user)
