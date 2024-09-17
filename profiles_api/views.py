from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

        an_apiview = [

        ]

        return Response({'messege': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        seralizer = self.serializer_class(data=request.data)

        if seralizer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'sa {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
