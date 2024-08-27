#!/bin/bash

# Activate the virtual environment (if applicable)
# source path/to/venv/bin/activate

# Update pip to the latest version
python3 -m pip install --upgrade pip

# Install requirements, excluding any lines mentioning 'apturl'
python3 -m pip install -r requirements.txt | grep -v "apturl"

# Collect static files
python3 manage.py collectstatic --no-input