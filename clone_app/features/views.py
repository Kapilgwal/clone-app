from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    return render(request, "home.html")

def search(request):
    return render(request, "search.html")

def reels(request):
    return render(request, "reels.html")

def myprofile(request):
    return render(request, "myprofile.html")

def posts(request):
    if request.method == "POST" and request.FILES.get("image"):
        image = request.FILES["image"]  
        
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        file_url = fs.url(filename)

        return render(request, "myprofile.html", {"file_url": file_url})

    return render(request, "myprofile.html")

