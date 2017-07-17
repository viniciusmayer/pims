pip install django
pip install djangorestframework
pip install psycopg2
pip install pika
pip install django-jenkins
pip install coverage

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

/**
Djanto-AMQP
http://pika.readthedocs.io/en/stable/

Django-PostgreSQL
http://initd.org/psycopg/docs/install.html

Django-Jenkings
https://github.com/kmmbvnr/django-jenkins

Django-RestFramework
http://www.django-rest-framework.org/tutorial/quickstart/
*/

# Project setup
'''
	git clone <url>
	virtualenv pims
	cd pims
	source bin/activate
	pip install django
	pip install psycopg2
	pip install pika
'''

# Run
'''
	cd pims
	source bin/activate
	python manage.py runserver
'''

# Database setup
* Create user
'''
CREATE USER pims WITH
	LOGIN
	SUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1
	PASSWORD 'viniciusmayer';
'''

* Create database
'''
CREATE DATABASE pims
    WITH 
    OWNER = pims
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;
'''