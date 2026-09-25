from langchain_qdrant import Qdrant
from langchain_huggingface import HuggingFaceEmbeddings
from src.core.config import settings

def get_hf_embeddings():
     return HuggingFaceEmbeddings(
         model = "BAAI/bge-m3",
         huggingfacehub_api_token = settings.huggingface_api_key
     )
     
def index_chunks(chunks, collection_name: str = "formations_docs"):
    
    Qdrant.from_documents(
        chunks,
        get_hf_embeddings(),
        url = settings.qdrant_url,
        collection_name = collection_name
    
    )