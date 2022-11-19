from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from aluraflix_api.core.serializers import RegisterSerializer


@api_view(['POST'])
def register(request):

    if request.method == 'POST':

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
