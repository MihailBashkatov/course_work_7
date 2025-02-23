from django.urls import path
from .views import HomeTemplateView, ReceiverCreateView, ReceiverUpdateView, ReceiverDetailView, ReceiverDeleteView, \
      MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, MailingPageTemplateView, \
      ChosenMailingPageTemplateView, ReceiverChosenView

app_name = 'mailing'

""" Registering URL adresses for mailing app"""
urlpatterns = [
      path('home/', HomeTemplateView.as_view(), name='home_template'),
      path('receiver/<int:pk>/', ReceiverDetailView.as_view(), name='receiver_detail'),
      path('receiver_create/', ReceiverCreateView.as_view(), name='receiver_create'),
      path('receiver_update/<int:pk>/', ReceiverUpdateView.as_view(), name='receiver_update'),
      path('receiver_delete/<int:pk>/', ReceiverDeleteView.as_view(), name='receiver_delete'),

      path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
      path('message_create/', MessageCreateView.as_view(), name='message_create'),
      path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
      path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),

      path('mailing/', MailingPageTemplateView.as_view(), name='mailing_page_template'),
      path('chosen_mailing/', ChosenMailingPageTemplateView.as_view(), name='chosen_mailing_page_template'),

      path('receiver/chosen/<int:pk>/', ReceiverChosenView.as_view(), name='receiver_chosen'),
]
