FROM python:3.11-slim

ENV PYTHONBUFFERED=1

RUN pip install uv

WORKDIR /app

COPY pyproject.toml

RUN uv pip install --system -r pyproject.toml

COPY src/ ./src/

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]