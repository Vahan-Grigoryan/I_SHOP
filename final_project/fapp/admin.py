from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe
from fapp.models import *


class CategoryAdmin(ModelAdmin):
    list_display = 'name', 'child_categories', 'products', 'both_images', 'id',
    search_fields = 'name',

    def products(self, instance):
        products = '<br>'.join(list(instance.products.values_list('name', flat=True)))
        return mark_safe(products)

    def child_categories(self, instance):
        children = '<br>'.join( list(instance.child_cats.values_list('name', flat=True)) )
        return mark_safe(children)

    def both_images(self, instance):
        html = ''
        if instance.image:
            html = f'<img src={instance.image.url} width="32" height="32">&nbsp;&nbsp;'
        if instance.image_replace:
            html += f'<img src={instance.image_replace.url}>'
        return mark_safe(html)

class BrandAdmin(ModelAdmin):
    list_display = '__str__', 'get_products',

    def get_products(self, instance):
        html = ''
        for product in instance.products.all():
            html+=product.__str__() + '<br>'
        return mark_safe(html)

class ProductAdmin(ModelAdmin):
    list_display = '__str__', 'stars_avg', 'image_miniatures', 'id',
    search_fields = 'name',

    def image_miniatures(self, instance):
        html = ''
        for image_instance in instance.images.all():
            html += f'<img src={image_instance.image.url} width="50" height="50" style="margin-right:20px" />'
        return mark_safe(html)

class ImageAdmin(ModelAdmin):
    list_display = 'rel_definition', 'thumbnail',

    def rel_definition(self, instance):
        return instance.product

    def thumbnail(self, instance):
        return mark_safe(f'<img src={instance.image.url} width="50" height="50" />')

class OrderAdmin(ModelAdmin):
    list_display = 'status', 'products_in_order',

    def products_in_order(self, instance):
        return tuple(instance.order_products.values_list('name', flat=True))


admin.site.register(User)
admin.site.register(Comment)
admin.site.register(IndependentMail)
admin.site.register(Blog)
admin.site.register(Order, OrderAdmin)
admin.site.register(BlogCategory)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
