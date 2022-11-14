from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from aluraflix_api.core.models import Categoria, Video
from aluraflix_api.core.serializers import VideoCategoriaSerializer, VideoSerializer


@api_view(['GET', 'POST'])
def videos_list_create(request):

    if request.method == 'GET':

        queryset = Video.objects.all()

        if search := request.query_params.get('search'):
            queryset = queryset.filter(titulo__icontains=search)

        serializer = VideoSerializer(queryset, many=True)

        return Response(data=serializer.data)

    elif request.method == 'POST':

        data = request.data

        serializer = VideoCategoriaSerializer(data=data)

        if serializer.is_valid():
            try:
                categoria = Categoria.objects.get(id=serializer.data['categoria_id'])
                data['categoria'] = categoria.pk
            except ObjectDoesNotExist:
                return Response(data={'error': 'Categoria inválida.'}, status=status.HTTP_409_CONFLICT)

        serializer = VideoSerializer(data=data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        video = serializer.save()

        serializer = VideoSerializer(instance=video)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
def videos_read_delete_update(request, id):

    try:
        video = Video.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = VideoSerializer(video)

        return Response(data=serializer.data)

    elif request.method == 'DELETE':

        video.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method in ['PUT', 'PATCH']:

        partial = True if request.method == 'PATCH' else False

        serializer = VideoSerializer(data=request.data, partial=partial)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.update(video, serializer.validated_data)

        return Response(status=status.HTTP_204_NO_CONTENT)
