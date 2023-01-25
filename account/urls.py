from django.urls import path
from .views import *


urlpatterns = [
    path('login/', Login, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('register/', Register, name='register'),
]
