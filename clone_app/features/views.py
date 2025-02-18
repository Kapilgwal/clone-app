from django.shortcuts import render, redirect
from .models import Posts  

def home(request):
    posts = Posts.objects.all()  # Fetch all posts
    return render(request, "home.html", {"posts": posts})  # Use "posts" instead of "post"

def search(request):
    return render(request, "search.html")

def reels(request):
    return render(request, "reels.html")

def myprofile(request):
    posts = Posts.objects.all()  # Fetch posts to display
    return render(request, "myprofile.html", {"posts": posts})  # Now posts is properly defined

def posts(request):
    if request.method == "POST" and request.FILES.get("image"):
        image = request.FILES["image"]
        
        post = Posts(image=image)  # Save uploaded image in database
        post.save()
        
        return redirect("myprofile")  # Redirect to profile after upload

    return render(request, "myprofile.html")
