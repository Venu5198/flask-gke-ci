# ---------- Build stage ----------
FROM python:3.13-slim AS builder

WORKDIR /app
COPY app/requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---------- Runtime stage ----------
FROM python:3.13-slim

# Security: non-root user
RUN useradd -m appuser

WORKDIR /app

COPY --from=builder /install /usr/local
COPY app/app.py .

USER appuser

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]

