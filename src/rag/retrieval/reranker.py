from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_community.document_compressors.cross_encoder import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from src.rag.retrieval.vectore_store import get_base_retriever

def get_hybrid_retriever(collection_name: str = "formation_docs"):
    base_retriever = get_base_retriever(collection_name)
    
    model = HuggingFaceCrossEncoder(model_name = "BAAI/bge-reranker-v2-m3")
    compressor = CrossEncoderReranker(model=model, top_n=5)
    
    return ContextualCompressionRetriever(
        base_compressor = compressor,
        base_retriever=base_retriever
    )