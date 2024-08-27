#!/bin/bash

# Activate the virtual environment (if applicable)
# source path/to/venv/bin/activate

# Install requirements without the 'apturl' package
python3 -m pip install -r requirements.txt --no-deps --upgrade apturl