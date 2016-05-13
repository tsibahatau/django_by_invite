Prerequisites:

Ensure django 1.8+ installed(use virtualenv or docker for that)

Follow next steps:

1) python manage.py createsuperuser
create superuser with any credentials your want to

2) python manage.py makemigrations invites
create migrations

3)python manage.py migrate
apply migrations

4)python manage.py test invites
run tests

5)python manage.py runserver
run server with invites app

login into http://127.0.0.1:8000/admin/ with superuser account and create Invite.
Checkout console for email logged and use url to create user. Login to http://127.0.0.1:8000/ with this credentials.
Logout.