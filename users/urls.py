from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import LoginUser, RegisterUser

app_name = 'users'

""" Registering URL adresses for users app"""
urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register_user'),

]