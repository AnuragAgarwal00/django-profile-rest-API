from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
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


class HelloViewSet(viewsets.ViewSet):
    """Test API viewsets"""
    serializer_class = HelloSerializer

    def list(self, request):
        """returns a string"""
        numbers = list(range(5))

        return Response({'numbers': numbers, 'message': 'list method'})

    def create(self, request):
        """Create a hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello, {name}'

            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Get a specific object"""
        return Response({'http_method': 'similar to get request'})

    def update(self, request, pk=None):
        """Update an object"""
        return Response({'http_method': 'similar to PUT request'})

    def partial_update(self, request, pk=None):
        """handle updating part of an object"""
        return Response({'http_method': 'similar to patch request'})

    def destroy(self, request, pk=None):
        """Handles removing an object"""
        return Response({'http_method': 'similar to delete request'})
