from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aluraflix_api.core.urls')),
    path('', include('aluraflix_api.videos.urls')),
]
