from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail


@shared_task
def ret_sum(num1, num2):
   print(num1+num2)
   return num1+num2