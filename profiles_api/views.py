from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self, request, format=None):

        an_apiview = [

        ]

        return Response({'messege': 'Hello!', 'an_apiview': an_apiview})


# Create your views here.
