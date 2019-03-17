# Slappy

---

## Slappy is a tool that listen on a slack channel for go message, when someone places the word go the slappy tool fetches feeds from FictionFone account and store them in the database

### Requirements

-   django
-   psycopg2-binary
-   slackclient
-   celery
-   python-twitter

## Installation

-   clone the repo and cd /path/to/repo
-   pip install pipenv
-   pipenv install
-   python manage.py makemigrations
-   python manage.py migrate
-   python manage.py runserver

### Configuration

-   after installing postgres you should create a database with the same name as in repo/settings.py in "DATABASE"
-   run 'celery -A Pain_Killer worker -l info' for background tasks
