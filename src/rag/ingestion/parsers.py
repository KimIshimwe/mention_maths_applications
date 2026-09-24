from llama_parse import LlamaParse
from src.core.config import settings

def parse_pdf(file_path: str) -> str:
    parser = LlamaParse(
        api_key = settings.llama_cloud_api_key,
        result_type = "markdown",
        verbose = False
    )
    parsed_docs = parser.load_data(file_path)
    return parsed_docs[0].text if parsed_docs else ""