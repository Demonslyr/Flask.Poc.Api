#! /usr/bin/env sh

# exit if script is called in a pipeline
set -e

export APP_MODULE="main:app"
export GUNICORN_CONF=/app/gunicorn_config.py
export GUNICORN_WORKER_CLASS="uvicorn.workers.UvicornWorker"

exec gunicorn -k "$GUNICORN_WORKER_CLASS" -c "$GUNICORN_CONF" "$APP_MODULE"
