from rest_framework.decorators import api_view
from rest_framework.response import Response

from aluraflix_api.core.models import Categoria
from aluraflix_api.core.serializers import CategoriaSerializer


@api_view()
def categorias_list_create(request):

    queryset = Categoria.objects.all()

    serializer = CategoriaSerializer(queryset, many=True)

    return Response(data=serializer.data)
