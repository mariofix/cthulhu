Cthulhu
======
![Cthulhu](https://media.giphy.com/media/3o85xzEtQs693ln3qM/giphy.gif)  
  
FullOn CRM for personal and commercial projects  

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)  

## Requirements
* Python 3.9 / Poetry
* MariaDB/MySQL
* Django 4.1

## Install
```bash
$ git init  
$ git remote add github git@github.com:mariofix/cthulhu.git  
$ git pull github base  
$ git checkout -B django-dev  
$ git pull github django-dev  
```

## Run
```bash
$ poetry install
$ poetry run python django-admin compilemessages
$ poetry run python manage.py migrate
$ poetry run python manage.py runserver
```
