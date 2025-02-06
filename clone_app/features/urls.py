from django.urls import path,include 
from .views import *
urlpatterns = [
    path('home/',home),
    path('reels/',reels),
    path('myprofile/',myprofile),
    path('search/',search),
]
