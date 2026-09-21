from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.dependencies import DBSession, CurrentUser

router = APIRouter()


@router.post("/sessions")
async def create_session(db: DBSession, user: CurrentUser):
    ...


@router.websocket("/ws/{session_id}")
async def chat_websocket(websocket: WebSocket, session_id: str):
    ...


@router.get("/sessions")
async def list_sessions(db: DBSession, user: CurrentUser):
    ...


@router.get("/sessions/{session_id}/messages")
async def get_messages(session_id: int, db: DBSession, user: CurrentUser):
    ...


@router.delete("/sessions/{session_id}")
async def delete_session(session_id: int, db: DBSession, user: CurrentUser):
    ...
