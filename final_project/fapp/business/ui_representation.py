from fapp.models import Brand, Category, Product


def get_formatted_categories_for_front(categories_position=None):
    """Return only center(that haven't parent and child categories) or nested categories"""
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
