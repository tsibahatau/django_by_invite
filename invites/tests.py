from django.core import mail
from django.test import TestCase

from invites.email_manager import send_registration_email
from invites.models import Invite
from invites.user_manager import user_create_from_invite


class NotificationEmailTest(TestCase):
    def test_send_registration_email(self):
        send_registration_email('test@test.com', 'userTest', 'password')
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "You are registered with following credentials:")
        self.assertEqual(mail.outbox[0].body, "\nYour credentials:\nLogin: userTest\nPassword: password")

    def test_invite_create(self):
        Invite.objects.create(email='test@email.com')
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "You are invited to django_by_invite. Whooora!")

    def test_user_create(self):
        invite = Invite.objects.create(email='test@email.com')
        user_create_from_invite(invite)
        self.assertEqual(len(mail.outbox), 2)
        self.assertEqual(mail.outbox[0].subject, "You are invited to django_by_invite. Whooora!")
        self.assertEqual(mail.outbox[1].subject, "You are registered with following credentials:")