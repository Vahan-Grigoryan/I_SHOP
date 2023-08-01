from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.utils import timezone
from rest_framework.generics import get_object_or_404
from fapp.models import User, SortViewedProducts, Product, Order, OrderedProductInfo, PayPalPayment


def add_or_del_viewed_product(user_pk, product_pk):
    """
    Add or delete user viewed product by logic like:
    if user viewed products > 10, remove last product(which was previously viewed by the user) and add new in first position,
    else just add product in user viewed products,
    if product already in viewed just change position to top.
    """
    user, product = User.objects.get(pk=user_pk), Product.objects.get(pk=product_pk)
    viewed_products = SortViewedProducts.objects.filter(user=user).order_by('-added_date')

    if user.viewed10_products.contains(product):
        product_to_top = viewed_products.get(product=product)
        product_to_top.added_date = timezone.now()
        product_to_top.save()

    if user.viewed10_products.count() > 10:
        product_for_del = viewed_products.last().product
        user.viewed10_products.remove(product_for_del)

    user.viewed10_products.add(product)

def add_order_product(post_data, user_pk, product_pk):
    """
    Add product into user order with null status,
    else create user order with null status and add products.
    Also point through model values for view user selected options for product.
    """
    user, product = User.objects.get(pk=user_pk), Product.objects.get(pk=product_pk)
    try:
        pending_order = user.orders.get(status__isnull=True)
        pending_order.order_products.add(
            product,
            through_defaults=dict(post_data.items())
        )

    except ObjectDoesNotExist:
        user.orders.create().order_products.add(
            product,
            through_defaults=dict(post_data.items())
        )

def del_order_product(user_pk, product_pk):
    """Del product from user order with null status"""
    user, product = User.objects.get(pk=user_pk), Product.objects.get(pk=product_pk)
    user.orders.get(status__isnull=True).order_products.remove(product)

def paypal_create_order(request, order_pk):
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

def paypal_capture_order_payment(order_pk):
    """Capture payment and change order status if payment successfully captured else delete payment method instance"""
    order = get_object_or_404(Order, id=order_pk)
    response = order.payment_method.capture_payment()
    if response.status_code == 201:

        order.status = 'pending'
        order.save()
    else:
        order.payment_method.delete()

    return response


def paypal_refund_order_payment(order_pk):
    """Refund payment and change order status if payment successfully refunded"""
    order = get_object_or_404(Order, id=order_pk)
    response = order.payment_method.refund_payment()
    if response.status_code == 201:
        order.status = 'rejected'
        order.save()

    return response

# products = OrderedProductInfo.objects.select_for_update().select_related('product').filter(order=order)