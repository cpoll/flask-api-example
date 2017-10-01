# Contributing Guidelines

## Getting Started:
- python3 -m venv venv && source venv/bin/activate
- pip install -r requirements-dev.txt && pip install -r requirements.txt

## Running uwsgi:
- uwsgi --http 0.0.0.0:5001 --processes 1 --module api.uwsgi --callable APP --master

## Running Tests:
