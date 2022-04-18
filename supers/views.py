from unicodedata import name
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import super_types
from super_types.models import Super_Types
from .serializers import SuperSerializer
from supers import serializers
from .models import Super
from django.shortcuts import get_object_or_404, get_list_or_404
from super_types import *

@api_view(['GET', 'POST'])
def supers_list(request):
    supers = Super.objects.all()
    if request.method == 'GET':
        type_param = request.query_params.get('type')
        
        if type_param:
            supers = supers.filter(super_type__type=type_param)
       
            serializer = SuperSerializer(supers, many=True)
            return Response(serializer.data)
        else:
            types = Super_Types.objects.all()
            custom_response_dictionary = {}

            for type in types:
                supers = Super.objects.filter(super_type_id=type.id)
                super_serializer = SuperSerializer(supers, many=True)
                custom_response_dictionary[type.type] = {
                    'Supers': super_serializer.data
                }

             

            return Response(custom_response_dictionary)


    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializers = SuperSerializer(supers)
        return Response(serializers.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        supers.delete
        return Response(status=status.HTTP_204_NO_CONTENT)

   