from django.urls import path

from .views import videos_list_create

app_name = "core"

urlpatterns = [
    path("videos", videos_list_create, name="videos-list-create"),
]
