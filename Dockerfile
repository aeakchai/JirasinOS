FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    TZ=Asia/Bangkok

ARG PUID=1007
ARG PGID=10

WORKDIR /app

# Create group if it doesn't exist, otherwise use existing group
RUN if getent group ${PGID} >/dev/null; then \
        EXISTING_GROUP=$(getent group ${PGID} | cut -d: -f1); \
    else \
        groupadd -g ${PGID} admin; \
        EXISTING_GROUP=admin; \
    fi && \
    useradd \
        --uid ${PUID} \
        --gid ${PGID} \
        --create-home \
        --shell /bin/bash \
        jack

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R ${PUID}:${PGID} /app

USER ${PUID}:${PGID}

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]