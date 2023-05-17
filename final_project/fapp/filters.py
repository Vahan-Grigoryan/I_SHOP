from django_filters import rest_framework as dfilters
from fapp.models import *


def filter_by_sale_new_hit(request_params):
    """Filter products by sale_new_hit property"""

    products = Product.objects.prefetch_related('images')
    sale_new_hit = request_params.get('sale_new_hit')
    products = filter(lambda p: sale_new_hit in p.sale_new_hit, products)

    return tuple(products)[:10]
