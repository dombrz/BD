from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Produkty
from polls.serializers import ProduktySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http import JsonResponse
from django.core import serializers




def index(request):
   
    tabela = Produkty.objects.all()
    serialized_tabela = serializers.serialize('json', tabela)
    print(serialized_tabela)
    return HttpResponse(serialized_tabela)
   
    