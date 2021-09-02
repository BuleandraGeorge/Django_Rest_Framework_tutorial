from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

@csrf_exempt
def snippet_list(request):
    if request.method=="GET":
        serializedSnippets = SnippetSerializer(Snippet.objects.all(), many=True)
        return JsonResponse(serializedSnippets.data, safe=False)
    
    elif request.method=="POST":
        data = JSONParser().parse(request)
        serializedSnippet = SnippetSerializer(data=data)
        if serializedSnippet.is_valid:
            serializedSnippet.save()
            return JsonResponse(serializedSnippet.data, status=201)
    return JsonResponse(serializedSnippet.errors, status=400)

@csrf_exempt
def snippet_details(request, snippet_id):
    try:
        the_snippet=Snippet.objects.get(pk=snippet_id)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method=="GET":
        ser_snip=SnippetSerializer(the_snippet)
        return JsonResponse(ser_snip.data, safe=False)

    """UPDATE"""
    if request.method=="PUT":
        snipet_data = JSONParser().parse(request)
        ser_snip = SnippetSerializer(the_snippet, data=snipet_data)
        if ser_snip.is_valid():
            ser_snip.save()
            return JsonResponse(ser_snip.data, status=201)
        return JsonResponse(ser_snip.errors, status=400)
    
    if request.method=="DELETE":
        the_snippet.delete()
        return HttpResponse(status=204)