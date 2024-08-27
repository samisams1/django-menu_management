#!/bin/bash

# Activate the virtual environment (if applicable)
# source path/to/venv/bin/activate

# Install requirements
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --no-input