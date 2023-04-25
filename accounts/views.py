from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Author
from .serializers import AuthorRegisterSerializer


class AuthorRegisterAPIView(viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorRegisterSerializer

    def create_author(self, request, is_staff):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            serializer.save(is_staff=is_staff)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False)
    def author(self, request, pk=None):
        return self.create_author(request, True)

    @action(methods=['post'], detail=False)
    def guest(self, request, pk=None):
        return self.create_author(request, False)


