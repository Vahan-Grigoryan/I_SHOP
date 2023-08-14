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

# @shared_task
# def send_approve_mail_for_order_receiving(user: dict, order: dict):
#     """
#     Send mail(with link for approve) to user for approve order receiving.
#     kwargs will contain keys:
#         user:
#             first_name,
#             email,
#
#         order:
#             id,
#             total_price,
#             code,
#     """
#     html_msg = \
#     f"""
#     <h1>Здравствуйте {user['first_name']}!</h1>
#     <p>Мы бы хотели убедиться что Вы успешно получили товары в заказе(общей стоимостью {order['total_price']}$)</p>
#     <p>Чтобы подтвердить это перейдите по ссылке:</p>
#     <а href="{settings.BACK_HOST}/paypal_receive_order/{order['id']}">{settings.BACK_HOST}/paypal_receive_order/{order['id']}</а>
#     <p>Tолько так вы можете поменять статус заказа на "received(полученный)"!</p>
#     """
#     send_mail(
#         f"Подтвердить получение заказа{order['code']}",
#         html_msg,
#         settings.EMAIL_HOST_USER,
#         (user['email'], ),
#         html_message=html_msg,
#     )