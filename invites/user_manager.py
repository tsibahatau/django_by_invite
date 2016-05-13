from django.contrib.auth.models import User

from django.template.loader import render_to_string
from django.core.mail import send_mail

from invites.models import Invite, UserProfile

from invites.email_manager import send_registration_email

def user_create_from_invite(invite):
    my_password = User.objects.make_random_password()
    user = User.objects.create_user(username=invite.email, email=invite.email,
                                    password=my_password)
    UserProfile.objects.create(user=user, invite_used=invite)
    invite.is_used = True
    invite.save()
    send_registration_email(invite.email, invite.email, my_password)
