#!/bin/bash
# One-command setup script for resumebuilder project

# create virtualenv and activate
python -m venv venv
source venv/bin/activate  # on Windows use "venv\\Scripts\\activate"

# install dependencies
pip install -r requirements.txt

# apply migrations and create superuser
python manage.py migrate

# collect static files
python manage.py collectstatic --noinput

echo "Setup complete. Activate the virtualenv and run python manage.py runserver"