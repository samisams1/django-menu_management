#!/bin/bash

# Activate the virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the required packages
.venv/bin/pip install -r requirements.txt

# Collect static files
.venv/bin/python manage.py collectstatic --no-input