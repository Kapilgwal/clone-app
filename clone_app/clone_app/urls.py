from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userAuth/',include('userAuth.urls')),
    path('features/',include('features.urls')),
]
