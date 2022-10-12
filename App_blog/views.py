from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserRegisterForm
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario,password=contra)
            if user is not None:
                login(request, user)
                usua=User.objects.filter(username__contains=usuario)
                return render(request, "user.html", {"usuario":usua})    
            else:
                return render(request,"index.html",{"mensaje":"datos incorrectos"})
        else:
            form = AuthenticationForm()
            return render(request,"index.html",{"form":form})
    form = AuthenticationForm()
    return render(request,"index.html",{"form":form})

def about(request):
    return render(request,"about.html")
def vista(request):
    form = AuthenticationForm()
    return render(request,"index.html",{"form":form})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"index.html",{"mensaje":"usuario creado con exito"})
    else:
        form=UserRegisterForm()
    return render(request,"register.html",{"form":form})


# Create your views here.

