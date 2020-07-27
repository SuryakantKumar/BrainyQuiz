# Introduction

This is a repository consisting of QuizApp named as 'Brainy Quiz'.
Install 'requirements.txt' if you want to use this project.

- Any user can register to brainy quiz and login with their registered username and password.

- Any user can create their own quizzess.

- Any user cna play quiz and the result will be shown to the user just after playing the quiz.

- Scores after playing the quiz will also be added to their respective id in the scoreboard.

## Directory Structure :

    quizapp
        ├── Dockerfile
        ├── QuizApp
        │   ├── __init__.py
        │   ├── __pycache__
        │   │   ├── __init__.cpython-37.pyc
        │   │   ├── settings.cpython-37.pyc
        │   │   ├── urls.cpython-37.pyc
        │   │   ├── views.cpython-37.pyc
        │   │   └── wsgi.cpython-37.pyc
        │   ├── settings.py
        │   ├── urls.py
        │   ├── views.py
        │   └── wsgi.py
        ├── README.md
        ├── docker-compose.yml
        ├── manage.py
        ├── nginx
        │   ├── Dockerfile
        │   └── nginx.conf
        ├── quiz
        │   ├── __init__.py
        │   ├── __pycache__
        │   │   ├── __init__.cpython-37.pyc
        │   │   ├── admin.cpython-37.pyc
        │   │   ├── forms.cpython-37.pyc
        │   │   ├── models.cpython-37.pyc
        │   │   ├── urls.cpython-37.pyc
        │   │   └── views.cpython-37.pyc
        │   ├── admin.py
        │   ├── apps.py
        │   ├── forms.py
        │   ├── migrations
        │   │   ├── 0001_initial.py
        │   │   ├── 0002_auto_20200620_1301.py
        │   │   ├── 0003_auto_20200620_1303.py
        │   │   ├── 0004_auto_20200620_1500.py
        │   │   ├── 0005_auto_20200620_1639.py
        │   │   ├── 0006_auto_20200625_1901.py
        │   │   ├── 0007_auto_20200626_0422.py
        │   │   ├── 0008_auto_20200629_1737.py
        │   │   ├── 0009_remove_question_answer.py
        │   │   ├── __init__.py
        │   │   └── __pycache__
        │   │       ├── 0001_initial.cpython-37.pyc
        │   │       ├── 0002_auto_20200620_1301.cpython-37.pyc
        │   │       ├── 0003_auto_20200620_1303.cpython-37.pyc
        │   │       ├── 0004_auto_20200620_1500.cpython-37.pyc
        │   │       ├── 0005_auto_20200620_1639.cpython-37.pyc
        │   │       ├── 0006_auto_20200625_1901.cpython-37.pyc
        │   │       ├── 0007_auto_20200626_0422.cpython-37.pyc
        │   │       ├── 0008_auto_20200629_1737.cpython-37.pyc
        │   │       ├── 0009_remove_question_answer.cpython-37.pyc
        │   │       └── __init__.cpython-37.pyc
        │   ├── models.py
        │   ├── templates
        │   │   └── quiz
        │   │       ├── category_detail.html
        │   │       ├── category_list.html
        │   │       ├── home.html
        │   │       ├── option_create.html
        │   │       ├── question_create.html
        │   │       ├── question_feature_ext.html
        │   │       ├── quiz_create.html
        │   │       ├── quiz_play.html
        │   │       ├── quiz_result.html
        │   │       └── scoreboard.html
        │   ├── tests.py
        │   ├── urls.py
        │   └── views.py
        ├── requirements.txt
        ├── staticfiles
        ├── templates
        │   ├── about.html
        │   ├── base.html
        │   ├── bootstrap.html
        │   ├── contact.html
        │   ├── footer.html
        │   ├── js.html
        │   └── navbar.html
        └── users
            ├── __init__.py
            ├── __pycache__
            │   ├── __init__.cpython-37.pyc
            │   ├── admin.cpython-37.pyc
            │   ├── forms.cpython-37.pyc
            │   ├── models.cpython-37.pyc
            │   └── views.cpython-37.pyc
            ├── admin.py
            ├── apps.py
            ├── forms.py
            ├── migrations
            │   ├── 0001_initial.py
            │   ├── 0002_delete_profile.py
            │   ├── __init__.py
            │   └── __pycache__
            │       ├── 0001_initial.cpython-37.pyc
            │       ├── 0002_delete_profile.cpython-37.pyc
            │       └── __init__.cpython-37.pyc
            ├── models.py
            ├── templates
            │   └── users
            │       ├── login.html
            │       ├── logout.html
            │       ├── profile.html
            │       └── register.html
            ├── tests.py
            └── views.py

## Instructions :

- To build the docker container, go the 'quizapp/app' directory and give command 'docker-compose build'

- To run the docker-container, got to 'quizapp/app' directory and give command 'docker-compose up'

- To create superuser, give command 'sudo docker-compose run web python manage.py createsuperuser'

- To make migrations to the postgreSQL database, give command 'sudo docker-compose run web python manage.py migrate'
