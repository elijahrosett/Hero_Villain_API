from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from supers import serializers
from .models import Super

from django.shortcuts import get_object_or_404, get_list_or_404


@api_view(['GET', 'POST'])
def supers_specific(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = serializers.SuperSerializer(super)
        #super = Super.objects.filter()
    
    
    return Response(serializer.data)

