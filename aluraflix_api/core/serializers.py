from rest_framework import serializers

from aluraflix_api.core.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            "id",
            "titulo",
            "descricao",
            "url",
        )
