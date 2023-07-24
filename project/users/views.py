from django.contrib.auth.models import User
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import UserSerializer

@api_view(['GET', 'POST'])
def base(request: Request):
    if request.method == 'POST':
        return createUser(request)
    elif request.method == 'GET':
        return getUsers(request)


def getUsers(request: Request):
    users = User.objects.all()
    response = []
    for user in users:
        response.append({
            'id': user.id,
            'username': user.username,
        })
    return Response(response)
    
def createUser(request: Request):
    username = request.data.get('username')
    password = request.data.get('password')

    try:
        userSerializer = UserSerializer(data={
            'username': username,
            'password': password
        })
        if userSerializer.is_valid():
            user = userSerializer.save()
        else: return Response(data=userSerializer.errors, status=400)
    except:
        return Response(status=400)
    
    return Response(data={ 'id': user.id }, status=201)