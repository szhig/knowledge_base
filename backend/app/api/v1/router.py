from fastapi import APIRouter

from app.api.v1 import auth, notes, documents, search, ai, graph, tags, spaces, users

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["认证"])
api_router.include_router(notes.router, prefix="/notes", tags=["笔记"])
api_router.include_router(documents.router, prefix="/documents", tags=["文档"])
api_router.include_router(search.router, prefix="/search", tags=["搜索"])
api_router.include_router(ai.router, prefix="/ai", tags=["AI 对话"])
api_router.include_router(graph.router, prefix="/graph", tags=["知识图谱"])
api_router.include_router(tags.router, prefix="/tags", tags=["标签"])
api_router.include_router(spaces.router, prefix="/spaces", tags=["知识空间"])
api_router.include_router(users.router, prefix="/users", tags=["用户"])
