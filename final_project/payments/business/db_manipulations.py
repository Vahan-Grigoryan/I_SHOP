import requests
from rest_framework.generics import get_object_or_404
from fapp.models import Order, User
from payments.models import PayPalPayment, StripePayment


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
    Capture payment and change order status if payment successfully captured
    else delete payment method instance
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


def stripe_create_card_owner(request):
    """Create StripePayment model and call create_customer"""
    stripe_payment = StripePayment.objects.create(user_id=request.user.id)

    return stripe_payment.create_customer(request.data)


def stripe_pay_order(user_pk, order_pk):
    """Pay pointed order with customer's card and change order status"""
    order = get_object_or_404(Order, id=order_pk)
    user = get_object_or_404(User, id=user_pk)
    order.payment_method = user.stripe_payment
    order.payment_method.create_and_pay_invoice(order)
    order.status = 'pending'
    order.save()
    return order


def stripe_refund_order(user_pk, order_pk):
    """Refund pointed order with customer's card and changing order status"""
    order = get_object_or_404(Order, id=order_pk)
    order.payment_method.create_refund()
    order.status = 'rejected'
    order.save()
    return order


