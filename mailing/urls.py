from django.urls import path
from .views import HomeTemplateView, ReceiverCreateView, ReceiverUpdateView, ReceiverDetailView, ReceiverDeleteView, \
      MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, MailingPageTemplateView, \
      MailingDetailView, MailingCreateView, MailingUpdateView, \
      MailingDeleteView, AttemptDetailView, AttemptCreateView, AttemptUpdateView, AttemptDeleteView, \
      StatisticsTemplateView, MailingListView, MailingDeactivateView, ReceiversListView, MessagesListView

app_name = 'mailing'

""" Registering URL adresses for mailing app"""
urlpatterns = [
      path('home/', HomeTemplateView.as_view(), name='home_template'),
      path('receiver/<int:pk>/', ReceiverDetailView.as_view(), name='receiver_detail'),
      path('receiver_create/', ReceiverCreateView.as_view(), name='receiver_create'),
      path('receiver_update/<int:pk>/', ReceiverUpdateView.as_view(), name='receiver_update'),
      path('receiver_delete/<int:pk>/', ReceiverDeleteView.as_view(), name='receiver_delete'),
      path('receivers_list/', ReceiversListView.as_view(), name='receivers_list'),

      path('message/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
      path('message_create/', MessageCreateView.as_view(), name='message_create'),
      path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
      path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
      path('messages_list/', MessagesListView.as_view(), name='messages_list'),

      path('mailings_list/', MailingListView.as_view(), name='mailing_list'),
      path('mailings_detail/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),
      path('mailings_create/', MailingCreateView.as_view(), name='mailing_create'),
      path('mailings_update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
      path('mailings_delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
      path('mailings/deactivate/<int:pk>/', MailingDeactivateView.as_view(), name='mailing_deactivate'),

      path('attempt_detail/<int:pk>/', AttemptDetailView.as_view(), name='attempt_detail'),
      path('attempt_create/', AttemptCreateView.as_view(), name='attempt_create'),
      path('attempt_update/<int:pk>/', AttemptUpdateView.as_view(), name='attempt_update'),
      path('attempt_delete/<int:pk>/', AttemptDeleteView.as_view(), name='attempt_delete'),


      path('mailing/', MailingPageTemplateView.as_view(), name='mailing_page_template'),
      path('statistics/', StatisticsTemplateView.as_view(), name='statistics'),

]
