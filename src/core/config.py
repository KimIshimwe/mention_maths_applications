from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    huggingface_api_key: str
    llama_cloud_api_key: str
    qdrant_url: str = "http://qdrant:6333"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        
settings = Settings()