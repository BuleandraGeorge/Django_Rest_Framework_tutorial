from django.http import Http404

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

#rest framework
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from .permissions import IsOwnerOrRead

permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrRead]

class SnippetList(generics.ListCreateAPIView):
    permission_classes=permission_classes
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=permission_classes
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
"""
class SnippetList(APIView, format=None):
    
    def get(self, *args, **kwargs):
        serializedSnippets = SnippetSerializer(Snippet.objects.all(), many=True)
        return Response(serializedSnippets.data)

    def post(self, *args, **kwargs):
        serializedSnippet = SnippetSerializer(data=request.data)
        if serializedSnippet.is_valid():
            serializedSnippet.save()
            return Response(serializedSnippet.data, status=status.HTTP_201_CREATED)
        return Response(serializedSnippet.errors, status=status.HTTP_404_NOT_FOUND)

class SnippetDetails(APIView, format=None):
    
    def get_object(self, pk):
        try:
           return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializedSnippet = SnippetSerializer(snippet)
        return Response(serializedSnippets.data)

    def put(self, request,pk, format=None):
        snippet=self.get_object(pk)
        serializedSnippet = SnippetSerializer(snippet, data=request.data)
        if serializedSnippet.is_valid():
            serializedSnippet.save()
            return Response(serializedSnippet.data, status=status.HTTP_201_CREATED)
        return Response(serializedSnippet.errors, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        snippet=self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
"""
@api_view(["GET", "POST"])
def snippet_list(request, format="json"):
    if request.method=="GET":
        serializedSnippets = SnippetSerializer(Snippet.objects.all(), many=True)
        return Response(serializedSnippets.data)
    
    elif request.method=="POST":
        serializedSnippet = SnippetSerializer(data=request.data)
        if serializedSnippet.is_valid():
            serializedSnippet.save()
            return Response(serializedSnippet.data, status=status.HTTP_201_CREATED)
    return Response(serializedSnippet.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET", "PUT", "DELETE"])
def snippet_details(request, snippet_id, format="api"):
    try:
        the_snippet=Snippet.objects.get(pk=snippet_id)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        ser_snip=SnippetSerializer(the_snippet)
        return Response(ser_snip.data)

    if request.method=="PUT":
        ser_snip = SnippetSerializer(the_snippet, data=request.data)
        if ser_snip.is_valid():
            ser_snip.save()
            return Response(ser_snip.data, status=status.HTTP_201_CREATED)
        return Response(ser_snip.errors, status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="DELETE":
        the_snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""