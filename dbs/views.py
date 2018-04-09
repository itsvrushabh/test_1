from django.shortcuts import render
from django.http.response import JsonResponse
from dbs.models import Steps, Workflow
from django.core import serializers
import json

# Create your views here.
def showDB(request):
    data = serializers.serialize("json",Steps.objects.all())
    
    json_object=json.loads(data)
    for i in json_object:
        print(i)

    return JsonResponse(data,safe=False,content_type='application/json')

