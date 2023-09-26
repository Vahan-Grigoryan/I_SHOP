from celery import shared_task
from django.core.mail import send_mail
from final_project import settings


@shared_task
def send_mail_as_task(subject, message, recipients):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        recipients,
        html_message=message,
    )