from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from supers import serializers
from .models import Super
from django.shortcuts import get_object_or_404, get_list_or_404

@api_view(['GET'])
def supers_list(request):

    if request.method == 'GET':
        products = Super.objects.all()
        serializer =SuperSerializer(products, many=True)
        return Response(serializer.data)

