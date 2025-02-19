from django.urls import path
from .views import HomeTemplateView

app_name = 'mailing'

""" Registering URL adresses for mailing app"""
urlpatterns = [
      path('home/', HomeTemplateView.as_view(), name='home_template'),

]
