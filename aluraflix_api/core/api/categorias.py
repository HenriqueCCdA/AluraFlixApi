from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from aluraflix_api.core.models import Categoria
from aluraflix_api.core.serializers import CategoriaSerializer, VideoSerializer


@api_view(['GET', 'POST'])
def categorias_list_create(request):

    if request.method == 'GET':
        queryset = Categoria.objects.all()

        serializer = CategoriaSerializer(queryset, many=True)

        return Response(data=serializer.data)

    elif request.method == 'POST':

        serializer = CategoriaSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        categoria = serializer.save()

        serializer = CategoriaSerializer(instance=categoria)

        headers = {'Location': categoria.get_absolute_url()}

        return Response(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
def categorias_read_delete_update(request, id):

    categoria = get_object_or_404(Categoria, id=id)

    if request.method == 'GET':

        serializer = CategoriaSerializer(instance=categoria)

        return Response(data=serializer.data)

    elif request.method == 'DELETE':

        categoria.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method in ['PUT', 'PATCH']:

        partial = True if request.method == 'PATCH' else False

        serializer = CategoriaSerializer(data=request.data, partial=partial)

        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.update(categoria, serializer.validated_data)

        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view()
def videos_by_categoria(request, id):

    categoria = get_object_or_404(Categoria, id=id)

    queryset = categoria.videos.all()

    serialize = VideoSerializer(queryset, many=True)

    return Response(data=serialize.data)
