FROM python:3.11-buster as builder

RUN pip install poetry==1.3.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --without dev --no-root

FROM python:3.11-slim-buster as runtime

ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app
COPY --from=builder /app/.venv .venv
COPY * .

ENTRYPOINT ["gunicorn", "-w", "8", "-b", "0.0.0.0", "--access-logfile=-", "main:app"]
