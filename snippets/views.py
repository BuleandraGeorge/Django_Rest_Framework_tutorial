from django.contrib.auth.models import User

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer

#rest framework
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, generics, permissions, viewsets, renderers

permissions_classes=[permissions.IsAuthenticatedOrReadOnly]

class SnippetViewSet(viewsets.ModelViewSet):
    queryset=Snippet.objects.all()
    serializer_class=SnippetSerializer
    permissions_classes

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
