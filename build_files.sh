#pip install -r requirements.txt 
#python3.9 manage.py collectstatic


#!/bin/bash

# Activate the virtual environment (if applicable)
# source path/to/venv/bin/activate

# Install requirements
python3.10 -m pip install -r requirements.txt

# Collect static files
python3.10 manage.py collectstatic --no-input