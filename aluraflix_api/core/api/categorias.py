from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from aluraflix_api.core.models import Categoria
from aluraflix_api.core.serializers import CategoriaSerializer


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
