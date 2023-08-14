"""
This module created for distribute logic in functions which used in project.
Also, this module include only functions, that forbidden to write in modules db_manipulations, ui_representation
"""
from django.utils import timezone
from fapp.tasks import send_mail_as_task
from final_project import settings


def get_order_receive_datetime(weekday=6, hour=17):
    """
    Return datetime for arrive_date field
    args:
        weekday: fixed day of week(for ex. saturday - 6)
        hour: fixed hour of weekday(for ex. 17)

    Consider above args mail will send at 17th hours of saturday
    """
    now = timezone.now()
    if now.isoweekday() < weekday:
        # if user pay order before weekday(on current week) - arrive date will be at weekday of current week
        naive_datetime = timezone.datetime(now.year, now.month, now.day, hour) + timezone.timedelta(
            days=weekday - now.isoweekday()
        )
    else:
        # if user pay order on or after weekday - arrive date will be next weekday
        naive_datetime = timezone.datetime(now.year, now.month, now.day, hour) + timezone.timedelta(
            days=7 - now.isoweekday() + weekday
        )

    return timezone.make_aware(naive_datetime)

def schedule_send_approval_mail(order):
    """Send mail on datetime in arrive_date for approve order receiving"""
    html_msg = \
    f"""
    <h1>Здравствуйте {order.user.first_name}!</h1>
    <p>Мы бы хотели убедиться что Вы успешно получили товары в заказе(общей стоимостью {order.total_price()}$)</p>
    <p>Чтобы подтвердить это перейдите по ссылке:</p>
    <а href="{settings.BACK_HOST}/paypal_receive_order/{order.id}">{settings.BACK_HOST}/paypal_receive_order/{order.id}</а>
    <p>Tолько так вы можете поменять статус заказа на "received(полученный)"!</p>
    """
    return send_mail_as_task.apply_async(
        (
            f"Подтвердить получение заказа{order.code()}",
            html_msg,
            (order.user.email,),
        ),
        eta=order.arrive_date
    )

def receive_question(request_data):
    if request_data.get('mail_msg_tel'):
        msg = f"tel: {request_data.get('mail_msg_tel')} \n\n{request_data.get('mail_msg_body')}"
    else:
        msg = request_data.get('mail_msg_body')

    send_mail_as_task.delay(
        request_data.get('mail_msg_name'),
        msg,
        (settings.EMAIL_HOST_USER,)
    )