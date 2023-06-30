from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from fapp.models import Brand, Category, Product, User, SortViewedProducts


def get_formatted_categories_for_front(categories_position=None):
    """Return nested categories"""
    result_categories = {}
    if categories_position == 'center':
        center_categories = Category.objects.filter(parent__isnull=False, child_cats__isnull=False).distinct()
        result_categories = tuple(center_categories.values('name', 'image'))
    else:
        left_categories = Category.objects.filter(parent__isnull=True).prefetch_related('child_cats')
        for category in left_categories:
            result_categories[category.name] = {}
            result_categories[category.name]['image'] = category.image.url
            result_categories[category.name]['image_replace'] = category.image_replace.url
            for child_cat in category.child_cats.all():
                result_categories[category.name][child_cat.name] = tuple(child_cat.child_cats.values_list('name', flat=True))
    
    return result_categories

def get_available_filters():
    """Return filters for front filters page"""
    brands = Brand.objects.values_list('name', flat=True)
    colors_raw = Product.objects.values_list('colors', flat=True)
    colors = []
    for color_str in colors_raw:
        colors = [*colors, *color_str.split(',')]

    colors = set(map(lambda color: color.strip(), colors))
    return {
        'brands': brands,
        'colors': colors,
    }

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

def add_order_product(user_pk, product_pk):
    """
    Add product into user order with pending status,
    else create user order with pending status and add products
    """
    user, product = User.objects.get(pk=user_pk), Product.objects.get(pk=product_pk)
    try:
        pending_order = user.orders.get(status='pending')
        pending_order.order_products.add(product)
    except ObjectDoesNotExist:
        user.orders.create(status='pending').order_products.add(product)

def del_order_product(user_pk, product_pk):
    """Del product from user order with pending status"""
    user, product = User.objects.get(pk=user_pk), Product.objects.get(pk=product_pk)
    user.orders.get(status='pending').order_products.remove(product)