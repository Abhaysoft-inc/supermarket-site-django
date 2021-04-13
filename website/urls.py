from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="homepage"),
    path('login/', login, name="loginpage"),
]
