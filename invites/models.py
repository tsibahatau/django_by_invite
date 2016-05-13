from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import pre_save


import uuid

from invites.email_manager import send_invite_email


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
        send_invite_email(instance.email, instance.key)

post_save.connect(send_user_email, sender=Invite)
