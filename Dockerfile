FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt pyproject.toml ./
RUN pip install --no-cache-dir -r requirements.txt

COPY rosetta ./rosetta
COPY rosetta-web/backend ./rosetta-web/backend

ENV PYTHONPATH=/app
ENV PORT=8008
EXPOSE 8008

CMD ["sh", "-c", "uvicorn backend.main:app --app-dir rosetta-web --host 0.0.0.0 --port ${PORT:-8008}"]
