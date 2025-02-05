from django.urls import path
from .views import login, signup, registration

urlpatterns = [
    path('login/', login, name="login"),  
    path('signup/', signup, name="signup"),
    path('userRegistration/', registration, name="registration"),
]
