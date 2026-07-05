#!/bin/bash

echo "===================================="
echo "Starting Azure DevOps Canary Demo..."
echo "===================================="

export PYTHONUNBUFFERED=1

gunicorn --bind=0.0.0.0:8000 \
          --workers=2 \
          --timeout=120 \
          app:app
