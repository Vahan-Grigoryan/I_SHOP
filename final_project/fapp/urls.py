from django.urls import path
from fapp import drf_views


urlpatterns = [
    path('categories', drf_views.Categories.as_view())
]