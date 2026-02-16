FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# install uv (via pip è ok e semplice in slim)
RUN pip install --no-cache-dir uv

# deps first (cache layer)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# app code
COPY . .

EXPOSE 8000
CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
