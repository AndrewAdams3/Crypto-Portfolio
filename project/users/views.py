from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User

# Create your views here.
def base(request: HttpRequest):
    if request.method == 'POST':
        createUser(request)


def createUser(request: HttpRequest):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    try:
        user = User.objects.create_user(username, email, password)
        user.save()
    except:
        return HttpResponse(status=400)
    
    return HttpResponse(status=201)