from fapp.models import Category


def get_formatted_categories_for_front(categories_position=None):
    result_categories = {}
    if categories_position == 'center':
        center_categories = Category.objects.filter(parent__isnull=False, child_cats__isnull=False).distinct()
        result_categories = tuple(center_categories.values('name', 'image'))
    else:
        left_categories = Category.objects.filter(parent__isnull=True)
        for category in left_categories:
            result_categories[category.name] = {}
            result_categories[category.name]['image'] = category.image.url
            result_categories[category.name]['image_replace'] = category.image_replace.url
            for child_cat in category.child_cats.all():
                result_categories[category.name][child_cat.name] = tuple(child_cat.child_cats.values_list('name', flat=True))
    
    return result_categories
