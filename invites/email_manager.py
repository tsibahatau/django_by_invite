from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


def send_registration_email(user_email, login, password):
    subject = "You are registered with following credentials:"
    message = render_to_string('invites/registration_email.txt', {'login': login, 'password': password})
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])


def send_invite_email(user_email, uuid):
    subject = "You are invited to django_by_invite. Whooora!"
    message = render_to_string('invites/invitation_email.txt', {'url': compose_url(str(uuid))})
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])


def compose_url(uuid):
    return settings.HOST_ADDRESS + '/createUser?invite=' + uuid