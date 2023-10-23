#!/bin/bash

if [ "$SERVICE" = "app" ]; then
    uvicorn app:app --host 0.0.0.0 --port 80
elif [ "$SERVICE" = "worker" ]; then
    celery -A tasks worker --loglevel=info
else
    echo "Unknown service type. Please set the SERVICE environment variable."
fi
