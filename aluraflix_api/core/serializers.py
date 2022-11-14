from rest_framework import serializers

from aluraflix_api.core.models import Categoria, Video


class VideoCategoriaSerializer(serializers.Serializer):
    categoria_id = serializers.IntegerField()


class VideoSerializer(serializers.ModelSerializer):
    # categoria_id = serializers.PrimaryKeyRelatedField(many=True, allow_null=True, required=False)

    class Meta:
        model = Video
        fields = (
            'id',
            'titulo',
            'descricao',
            'url',
            'categoria'
        )


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = (
            'id',
            'titulo',
            'cor',
        )
