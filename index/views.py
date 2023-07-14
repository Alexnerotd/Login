from django.shortcuts import render
from .models import Login
# Create your views here.


def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']


        login_data = Login(name=name, password=password, email=email)
        login_data.save()

    return render(request, 'login.html')