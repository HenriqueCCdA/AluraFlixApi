from django.urls import path

from .api.categorias import (
    categorias_list_create,
    categorias_read_delete_update,
    videos_by_categoria,
)
from .api.videos import videos_list_create, videos_read_delete_update

app_name = 'core'

urlpatterns = [
    # videos
    path('videos/', videos_list_create, name='videos-list-create'),
    path('videos/<int:id>', videos_read_delete_update, name='videos-read-delete-update'),
    # categorias
    path('categorias/', categorias_list_create, name='categoria-list-create'),
    path('categorias/<int:id>', categorias_read_delete_update, name='categoria-read-delete-update'),
    path('categorias/<int:id>/videos/', videos_by_categoria, name='videos-by-categoria'),
]
