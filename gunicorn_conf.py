import os


def _int_env(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None or value == "":
        return default
    return int(value)


bind = f"0.0.0.0:{os.getenv('PORT', '8000')}"
worker_class = "uvicorn.workers.UvicornWorker"
workers = _int_env("WORKERS", 5)

# Long provider streams should not be interrupted by the default 30s graceful
# shutdown window, and workers should not recycle while streaming requests run.
timeout = _int_env("GUNICORN_TIMEOUT", 300)
graceful_timeout = _int_env("GUNICORN_GRACEFUL_TIMEOUT", 300)
keepalive = _int_env("GUNICORN_KEEPALIVE", 75)
max_requests = _int_env("GUNICORN_MAX_REQUESTS", 0)
max_requests_jitter = _int_env("GUNICORN_MAX_REQUESTS_JITTER", 0)
