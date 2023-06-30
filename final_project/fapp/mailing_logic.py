from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.db import IntegrityError

from fapp.models import IndependentMail, User
from final_project import settings



def send_first_mail_and_add_to_mail_list(mail=None):
    """
    Send 'welcome' email to new email and add new IndependentMail if User with that new email does not exist.
    """
    try:
        user = User.objects.get(email=mail)
        user.in_mailing_list = True
        user.save()
        return {'Message': f'User mail subscribed successfully, check it!'}
    except ObjectDoesNotExist:
        try:
            IndependentMail.objects.create(mail=mail)
            send_mail(
                '(from Bernu Veikals)Experimental first message to your mail',
                'Thanks for subscribing to this mailing list,'
                'as you already understood, I made this opportunity without need registration,'
                'why? Because I so want!. If you will like some product from the mailing list,'
                'you will register yourself and buy\U0001F604\U0001F603\U0001F601',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=(mail,)
            )
            return {'Message': f'Independent mail subscribed successfully, check it!'}
        except IntegrityError:
            return {'Error': 'Mail already exist!'}

def del_mail_from_mail_list(mail=None):
    """Similar send_first_mail_and_add_to_mail_list but does the opposite"""
    try:
        user = User.objects.get(email=mail)
        user.in_mailing_list=False
        user.save()
        return {'Message': f'User mail deleted from mail list successfully'}
    except ObjectDoesNotExist:
        try:
            independent_mail = IndependentMail.objects.get(mail=mail)
            independent_mail.delete()
            return {'Message': f'Independent mail deleted successfully'}
        except ObjectDoesNotExist:
            return {"Error" : "Mail didn't match!"}

def send_msg_to_all_mails(subject=None, msg=None):
    """Send mail to all IndependentMail and User objects"""
    independent_mails = IndependentMail.objects.values_list('mail', flat=True)
    user_mails = User.objects.filter(in_mailing_list=True).values_list('email', flat=True)
    send_mail(
        subject,
        msg,
        settings.EMAIL_HOST_USER,
        [*independent_mails, *user_mails]
    )
