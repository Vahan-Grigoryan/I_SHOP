from django_filters import rest_framework as dfilters
from fapp.models import *


def filter_by_sale_new_hit(request_params):
    """Filter products by sale_new_hit property"""

    products = Product.objects.prefetch_related('images')
    sale_new_hit = request_params.get('sale_new_hit')
    products = filter(lambda p: sale_new_hit in p.sale_new_hit, products)

    return tuple(products)[:10]

class ProductFilter(dfilters.FilterSet):
    name = dfilters.CharFilter(field_name='name', lookup_expr='icontains')
    categories = dfilters.BaseInFilter(field_name='category__name', lookup_expr='in')
    brands = dfilters.BaseInFilter(field_name='brand__name', lookup_expr='in')
    priceGte = dfilters.NumberFilter(method='get_price_sailed_price_gte')
    priceLte = dfilters.NumberFilter(method='get_price_sailed_price_lte')
    colors = dfilters.BaseInFilter(method='colors_in')

    def get_filtered_prices(self, queryset, price, lte_or_gte):
        """
        If product have saled_price filtering will be carried out on saled_price else price field.
        This func can be called for priceGte priceLte filtering fields above.
        """
        if lte_or_gte == 'gte':
            qs = queryset.filter(saled_price__isnull=False, saled_price__gte=price)
            qs |= queryset.filter(saled_price__isnull=True, price__gte=price)
        else:
            qs = queryset.filter(saled_price__isnull=False, saled_price__lte=price)
            qs |= queryset.filter(saled_price__isnull=True, price__lte=price)
        return qs

    def get_price_sailed_price_gte(self, queryset, name, price):
        return self.get_filtered_prices(queryset, price, 'gte')

    def get_price_sailed_price_lte(self, queryset, name, price):
        return self.get_filtered_prices(queryset, price, 'lte')

    def colors_in(self, queryset, name, colors):
        """
        colors = colors url param = for ex. ['red', 'blue']
        return products according selected logic below
        logic 1: all selected colors must be in each product
        logic 2: at least one color of selected must be in each product
        """
        # logic 1
        qs = queryset.filter(colors__icontains=colors[0])
        if len(colors) == 1:
            return qs
        else:
            for color in colors[1:]:
                qs &= qs.filter(colors__icontains=color)
            return qs

        # logic 2
        # qs = Product.objects.none()
        # for color in colors:
        #     qs |= queryset.filter(colors__icontains=color)
        # return qs

    class Meta:
        model = Product
        fields = 'categories', 'brands', 'priceGte', 'priceLte', 'colors'

class BlogFilters(dfilters.FilterSet):
    category = dfilters.CharFilter(field_name='category__name')
    class Meta:
        model = Blog
        fields = 'category',