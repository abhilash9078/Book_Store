from django.core.mail import EmailMessage
from celery import shared_task


class Util:
    @staticmethod
    @shared_task
    def send_email(data):
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            from_email='princeabhi966@gmail.com',
            to=[data['to_email']]
        )
        email.send()



