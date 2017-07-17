wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
sudo pip install -U pip
sudo pip install -U Django
sudo pip install -U psycopg2
sudo pip install -U djangorestframework
sudo pip install -U pika
sudo pip install django-jenkins
sudo pip install coverage

sudo apt-get install python-dev
sudo pip install https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v1.5/pip/pgadmin4-1.5-py2.py3-none-any.whl

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