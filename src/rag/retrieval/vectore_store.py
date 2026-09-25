from langchain_qdrant import Qdrant
from qdrant_client import QdrantClient
from src.core.config import settings
from src.rag.ingestion.indexers import get_hf_embeddings

def get_base_retriever(collection_name: str= "formation_docs"):
    client = QdrantClient(url=settings.qdrant_url)
    qdrant = Qdrant(
        client = client,
        collection_name=collection_name,
        embeddings = get_hf_embeddings()
        
    )
    return qdrant.as_retriever(search_kwargs={"k":50})

    
    
    
    
    