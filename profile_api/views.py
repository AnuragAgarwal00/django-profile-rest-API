from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):

    def get(self, request, format=None):
        numbers = list(range(11))

        return Response({'numbers': numbers, 'message': 'hello'})
