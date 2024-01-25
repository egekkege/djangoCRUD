#!/bin/bash
echo "Creating Migrations..."
python3 manage.py makemigrations
echo ====================================

echo "Starting Migrations..."
python3 manage.py migrate
echo ====================================
source .venv/bin/activate
#python3 manage.py startapp testdb
echo "Starting Server..."
python3 manage.py runserver