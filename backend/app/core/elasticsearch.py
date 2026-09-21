from elasticsearch import AsyncElasticsearch

from app.config import settings

es_client = AsyncElasticsearch(hosts=[settings.ELASTICSEARCH_URL])

NOTES_INDEX_MAPPING = {
    "mappings": {
        "properties": {
            "note_id": {"type": "long"},
            "title": {
                "type": "text",
                "analyzer": "ik_max_word",
                "search_analyzer": "ik_smart",
            },
            "content": {
                "type": "text",
                "analyzer": "ik_max_word",
                "search_analyzer": "ik_smart",
            },
            "excerpt": {"type": "text", "analyzer": "ik_max_word"},
            "tags": {"type": "keyword"},
            "user_id": {"type": "keyword"},
            "space_id": {"type": "keyword"},
            "status": {"type": "keyword"},
            "is_pinned": {"type": "boolean"},
            "word_count": {"type": "integer"},
            "created_at": {"type": "date"},
            "updated_at": {"type": "date"},
            "embedding": {
                "type": "dense_vector",
                "dims": settings.EMBEDDING_DIMS,
                "index": True,
                "similarity": "cosine",
            },
        }
    }
}

DOCUMENTS_INDEX_MAPPING = {
    "mappings": {
        "properties": {
            "document_id": {"type": "long"},
            "chunk_index": {"type": "integer"},
            "title": {
                "type": "text",
                "analyzer": "ik_max_word",
                "search_analyzer": "ik_smart",
            },
            "content": {
                "type": "text",
                "analyzer": "ik_max_word",
                "search_analyzer": "ik_smart",
            },
            "file_type": {"type": "keyword"},
            "user_id": {"type": "keyword"},
            "space_id": {"type": "keyword"},
            "metadata": {"type": "object", "enabled": False},
            "created_at": {"type": "date"},
            "embedding": {
                "type": "dense_vector",
                "dims": settings.EMBEDDING_DIMS,
                "index": True,
                "similarity": "cosine",
            },
        }
    }
}


async def init_indices() -> None:
    """Create Elasticsearch indices if they don't exist."""
    for index_name, mapping in [
        (settings.ES_NOTES_INDEX, NOTES_INDEX_MAPPING),
        (settings.ES_DOCUMENTS_INDEX, DOCUMENTS_INDEX_MAPPING),
    ]:
        exists = await es_client.indices.exists(index=index_name)
        if not exists:
            await es_client.indices.create(index=index_name, body=mapping)


async def close_es() -> None:
    await es_client.close()
