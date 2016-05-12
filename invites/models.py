from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

import uuid

class Invite(models.Model):
    email = models.CharField(max_length=200)
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_used = models.BooleanField(default=False)

    def __unicode__(self):
        return self.email



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    invite_used = models.OneToOneField(Invite)


def send_user_email(sender, instance=None, **kwargs):
    if kwargs['created'] and instance:
        subject = "You are invited to django_by_invite. Whooora!"
        message = render_to_string('invites/invitation_email.txt',{'url': compose_url(instance)})
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.email])

post_save.connect(send_user_email, sender=Invite)

def compose_url(instance):
    return 'http://127.0.0.1:8000/createUser?invite=' + str(instance.key)