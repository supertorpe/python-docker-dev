#!/bin/bash

/opt/venv/bin/pip install -r /app/requirements.txt
cd /app
if [[ "$ENTRYPOINT" == "shell" ]]; then
  exec /bin/bash
else
  /opt/venv/bin/python /app/main.py
fi
