from django.contrib import admin

from aluraflix_api.videos.models import Categoria, Video

admin.site.register(Video)
admin.site.register(Categoria)
