from rest_framework import serializers

from aluraflix_api.core.models import Categoria, Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            'id',
            'titulo',
            'descricao',
            'url',
        )


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = (
            'id',
            'titulo',
            'cor',
        )
