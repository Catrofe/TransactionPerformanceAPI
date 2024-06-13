FROM python:3.11-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml .
COPY src /app/src

RUN pip install poetry
RUN poetry install

CMD ["poetry", "run", "uvicorn", "src.app:app"]
