# Knowledge Base

个人笔记知识库 — Markdown 双向链接 + AI RAG 问答 + 全文搜索

## 技术栈

- **后端**: FastAPI + SQLAlchemy 2.0 + Celery
- **前端**: Vue 3 + TypeScript + Vite + Naive UI
- **数据库**: MySQL 8.0 + Elasticsearch 8.x
- **缓存**: Redis 7
- **存储**: MinIO (S3 兼容)
- **AI**: LangChain + OpenAI/Anthropic

## 快速开始

### 1. 启动基础设施

```bash
make docker-up
```

### 2. 安装依赖

```bash
make install
```

### 3. 配置环境变量

```bash
cp backend/.env.example backend/.env
# 编辑 .env 文件，填入 LLM API Key 等配置
```

### 4. 初始化数据库

```bash
make migrate-run
```

### 5. 启动开发服务

```bash
make dev
```

- 后端 API: http://localhost:8000/docs
- 前端: http://localhost:5173

## 项目结构

```
knowledge_base/
├── backend/          # FastAPI 后端
├── frontend/         # Vue 3 前端
├── docker-compose.yml
├── Makefile
└── docs/            # 设计文档
```

## 核心功能

- Markdown 笔记编辑 + 双向链接 `[[]]`
- 知识图谱可视化
- 文档上传与解析 (PDF/Word/Markdown/HTML)
- AI 智能问答 (RAG)
- Elasticsearch 全文搜索 + 语义搜索
- 用户认证 + 知识空间协作
