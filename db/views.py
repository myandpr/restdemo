# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


"""
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from db.models import Person
from db.serializers import PersonSerializer
"""

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from db.models import Person
from db.serializers import PersonSerializer



from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO
# Create your views here.


"""
@csrf_exempt
def person_list(request):
    if request.method == 'GET':
        snippets = Person.objects.all()
        serializer = PersonSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
"""



@api_view(['GET', 'POST'])
def person_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Person.objects.all()
        serializer = PersonSerializer(snippets, many=True)
        return Response(serializer.data)

        #return json format data
        """
        content = JSONRenderer().render(serializer.data)
        return Response(content)
       """

    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        print(type(request.data))
        print(request.data["name"],request.data["age"])
        if serializer.is_valid():
            serializer.save()
            print("success")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("faild")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

