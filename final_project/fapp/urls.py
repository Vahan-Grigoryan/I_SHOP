from django.urls import path
from fapp import drf_views


urlpatterns = [
    path('mailing_list', drf_views.MailingList.as_view()),
    path('receive_mail', drf_views.ReceiveQuestion.as_view()),
    path('categories', drf_views.CategoryList.as_view()),
    path('category_children/<str:category_name>', drf_views.CategoryChildren.as_view()),
    path('brands_index', drf_views.BrandIndexList.as_view()),
    path('blogs_index', drf_views.BlogIndexList.as_view()),
    path('products_index', drf_views.ProductIndexList.as_view()),
    path('products/<int:pk>', drf_views.ProductDetail.as_view()),

]