# Project setup
'''
	wget https://bootstrap.pypa.io/get-pip.py
	python get-pip.py
	sudo pip install -U pip
	git clone <url>
	virtualenv pims
	cd pims
	source bin/activate
	pip install django
	pip install psycopg2
	pip install pika
	pip install coverage

	python manage.py migrate
	python manage.py createsuperuser
	python manage.py runserver

'''

# Shell
'''
	python manage.py shell
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

# PGAdmin 4 - On *Unix
'''
	sudo apt-get install python-dev
	sudo pip install https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v1.5/pip/pgadmin4-1.5-py2.py3-none-any.whl
'''

# References
* Djanto-AMQP: http://pika.readthedocs.io
* Django-PostgreSQL: http://initd.org/psycopg/docs
* Kafka Python: http://kafka-python.readthedocs.io