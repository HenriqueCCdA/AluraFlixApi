from django.urls import path

from .views import videos_list_create, videos_read_delete_update

app_name = "core"

urlpatterns = [
    path("videos/", videos_list_create, name="videos-list-create"),
    path(
        "videos/<int:id>", videos_read_delete_update, name="videos-read-delete-update"
    ),
]
