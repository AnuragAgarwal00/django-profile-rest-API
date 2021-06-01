from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer


class HelloAPIView(APIView):
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        numbers = list(range(11))

        return Response({'numbers': numbers, 'message': 'hello'})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello, {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """handle updating the objects"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partical update of an object"""
        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """deleting objects"""
        return Response({'method': 'delete'})
