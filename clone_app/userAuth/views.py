from django.shortcuts import render, HttpResponse, redirect
from .models import Registration
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login

def login(request):
    if request.method == "POST": 
        username = request.POST.get("username")
    
        password = request.POST.get("password")

        if not Registration.objects.filter(username=username).exists():
            return HttpResponse(" Please give a valid username.")

        

        hashed_password = make_password(password)
        
        user = authenticate(request,username = username,password = hashed_password)
        

        return HttpResponse("You signed in successfully")  

    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def registration(request):
    if request.method == "POST": 
        username = request.POST.get("username")
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        password = request.POST.get("password")

        if Registration.objects.filter(username=username).exists():
            return HttpResponse("Username is not unique, please choose another one.")

        if not all([username, name, email, age, password]):
            return HttpResponse("All fields are required.")

        hashed_password = make_password(password)

        user = Registration(username=username, name=name, email=email, age=age, password=hashed_password)
        user.save()

        return redirect("login")  

    return render(request, "signup.html")
