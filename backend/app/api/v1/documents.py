from fastapi import APIRouter

from app.dependencies import DBSession, CurrentUser

router = APIRouter()


@router.post("/upload")
async def upload_document(db: DBSession, user: CurrentUser):
    ...


@router.get("/")
async def list_documents(db: DBSession, user: CurrentUser):
    ...


@router.get("/{document_id}")
async def get_document(document_id: int, db: DBSession, user: CurrentUser):
    ...


@router.get("/{document_id}/content")
async def get_document_content(document_id: int, db: DBSession, user: CurrentUser):
    ...


@router.delete("/{document_id}")
async def delete_document(document_id: int, db: DBSession, user: CurrentUser):
    ...
