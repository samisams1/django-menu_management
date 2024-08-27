#!/bin/bash

# Activate the virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the required packages
pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --no-input