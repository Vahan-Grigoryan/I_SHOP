from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from fapp.models import User, SortViewedProducts, Product


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
    """
    Del product from user order with null status,
    if after delete order haven't any product delete it
    """
    user, product = User.objects.get(pk=user_pk), Product.objects.get(pk=product_pk)
    order = user.orders.get(status__isnull=True)
    order.order_products.remove(product)
    if not order.order_products.count():
        order.delete()

