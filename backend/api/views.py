from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .sers import *

# Create your views here.
@api_view(['POST'])
def login(request):
    return Response(request.data)

@api_view(['POST'])
def Register(request):
    return Response()
