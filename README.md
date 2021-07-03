# Setup
## Docker
```
    ref: [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu eoan stable"
    sudo apt-get install docker-ce docker-ce-cli containerd.io
```

## Postgres
* install
```
    sudo apt install docker-compose
    sudo groupadd docker
    sudo usermod -aG docker $USER
    newgrp docker
    sudo systemctl enable docker
    docker-compose -f postgres.yml up
```

* create user

```
CREATE USER pims WITH
	LOGIN
	SUPERUSER
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	CONNECTION LIMIT -1
	PASSWORD 'p1m5';
```

* create database

```
CREATE DATABASE pims
    WITH 
    OWNER = pims
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;
```

* or alter database owner 

```
ALTER DATABASE pims OWNER TO pims;
```

## Project
* install pip and virtualenv
```
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py
    sudo pip install -U pip
    sudo pip install virtualenv
```

* project setup

```
	git clone <url>
	virtualenv pims
	cd pims
	source bin/activate
	pip install django
	pip install psycopg2-binary
	pip install pika
	pip install coverage
```

* database setup

```
    python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py createsuperuser
	python3 manage.py runserver
```

* run

```
	cd pims
	source bin/activate
	python3 manage.py runserver
```

# PGAdmin 4 - On *Unix
```
	sudo apt-get install python-dev
	sudo pip install https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v1.5/pip/pgadmin4-1.5-py2.py3-none-any.whl
```

# References
* Djanto-AMQP: http://pika.readthedocs.io/en/stable/
* Django-PostgreSQL: http://initd.org/psycopg/docs/install.html
