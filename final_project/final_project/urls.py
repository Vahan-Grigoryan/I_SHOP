from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from final_project import settings

urlpatterns = [
    path('', include('fapp.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
