from django.urls import path
from .views import HomeTemplateView, ReceiverCreateView, ReceiverUpdateView, ReceiverDetailView, ReceiverDeleteView

app_name = 'mailing'

""" Registering URL adresses for mailing app"""
urlpatterns = [
      path('home/', HomeTemplateView.as_view(), name='home_template'),
      path('receiver/<int:pk>/', ReceiverDetailView.as_view(), name='receiver_detail'),
      path('create/', ReceiverCreateView.as_view(), name='receiver_create'),
      path('update/<int:pk>/', ReceiverUpdateView.as_view(), name='receiver_update'),
      path('delete/<int:pk>/', ReceiverDeleteView.as_view(), name='receiver_delete'),
]
