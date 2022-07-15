from django.shortcuts import render
from django.http import HttpResponse
from index.models import Contect
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, 'project.html')


def contect(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        concern = request.POST['concern']
        print(name, email, phone, concern)
        obj = Contect(name=name, email=email, phone=phone, concern=concern)
        obj.save()
    return render(request, 'contect.html')
