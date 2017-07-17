rm -rf ../coverage/*
coverage run --source='../' --omit="../backend/migrations/*,../pims/*,../scrips/*,../files/*,../docs/*,../*/__*,../*/tests.py,../*/builders.py,../backend/admin.py,../backend/forms.py,../manage.py" ../manage.py test backend
coverage html --directory="../coverage/"