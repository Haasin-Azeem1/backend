from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .sers import *
from django.contrib.auth.models import User
from .models import *
import uuid

# Create your views here.
@api_view(['POST'])
def login(request):
    return Response(request.data)

@api_view(['POST'])
def Register(request):
    email = request.POST['email']
    number = request.POST['number']
    password = request.POST['password']
    session = myuuid = uuid.uuid4()

    user = User.objects.create_user(email, password)
    user1 = UserModel.objects.create(user_id = user.id, number = number, email = email, session = session)

    return Response(UserSer(user1).data)