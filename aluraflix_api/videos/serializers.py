from rest_framework import serializers

from aluraflix_api.videos.models import Categoria, Video


class VideoCategoriaSerializer(serializers.Serializer):
    categoria_id = serializers.IntegerField()


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'titulo', 'descricao', 'url', 'categoria')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'titulo', 'cor')
