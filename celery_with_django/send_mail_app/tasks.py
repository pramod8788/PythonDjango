from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from celery_with_django import settings

@shared_task(bind=True)
def send_mails_func(self):
    users = get_user_model().objects.all()
    for user in users:
        messasge_subject = "Hi! Testing"
        message = "Testing to send emails through django celery"
        to_mail = user.email
        send_mail(
            subject=messasge_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_mail],
            fail_silently=True
        )

    return "Sending mails Done"