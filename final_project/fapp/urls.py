from django.urls import path
from fapp import drf_views


urlpatterns = [
    path('', drf_views.Index.as_view())
]