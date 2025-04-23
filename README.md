# Now or Never
## Task scheduler

The first self-written simple program for organizing notes,
in python 3.11 and django 4.2.

The goal of the project is to use and consolidate my knowledge of django and python in practice


Profile photo:

<img alt="Profile photo" src="https://github.com/AgvanGrigoryan/todo_server/assets/101641443/6590bf49-e87b-4e0a-a2b3-9d8dcd5c4132" width="750px"><br>


Task list:

<img alt="Task List" src="https://github.com/AgvanGrigoryan/todo_server/assets/101641443/d5139278-e5b5-4d27-a984-93bee795059e" width="750px"><br>


Task detail:

<img alt="Profile photo" src="https://github.com/AgvanGrigoryan/todo_server/assets/101641443/995a7a2b-f434-43db-850e-ad9bda7b09b0" width="750px"><br>


Today tasks:

<img alt="Profile photo" src="https://github.com/AgvanGrigoryan/todo_server/assets/101641443/3ec3dbe0-b81e-4bb2-943c-3744af3f7eb8" width="750px">


## How To Build
- git clone git@github.com:AgvanGrigoryan/todo_server.git
- cd todo_server
- python -m venv venv && source venv/bin/activate
- pip install -r now_or_never/requirements.txt
- python now_or_never/manage.py makemigrations && python now_or_never/manage.py migrate
- python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
- echo 'DJANGO_SECRET_KEY="__PREVIOUS_COMMAND_GENERATED_OUTPUT__"' > now_or_never/.env
- python manage.py createsuperuser
- python manage.py runserver
- Login as admin login, password and ENJOY :)
