import requests
from rest_framework.generics import get_object_or_404
from fapp.models import Order, PayPalPayment



def paypal_create_order(request, order_pk) -> str:
    """
    Create PayPalPayment instance and immediately relate with order,
    also create PayPal order and return approve_url for redirect.
    """
    order = get_object_or_404(Order, id=order_pk)
    paypal_payment = PayPalPayment.objects.create()
    order.payment_method = paypal_payment
    order.save()
    approve_url = paypal_payment.create_order(
        request,
        order,
        request.data.get('approved_url'),
        request.data.get('cancel_url'),
    )
    return approve_url

def paypal_capture_order_payment(order_pk) -> requests.Response:
    """
    Capture payment and change order status if payment successfully captured else delete payment method instance
    """
    order = get_object_or_404(Order, id=order_pk)
    response = order.payment_method.capture_payment()
    if response.status_code == 201:
        order.status = 'pending'
        order.save()
    else:
        order.payment_method.delete()

    return response

def paypal_receive_order(order_pk) -> Order:
    """Approve order receiving"""
    order = get_object_or_404(Order, id=order_pk)
    order.status = 'received'
    order.save()
    return order

def paypal_refund_order_payment(order_pk) -> requests.Response:
    """Refund payment and change order status if payment successfully refunded"""
    order = get_object_or_404(Order, id=order_pk)
    response = order.payment_method.refund_payment()
    if response.status_code == 201:
        order.status = 'rejected'
        order.save()

    return response