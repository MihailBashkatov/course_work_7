from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView

from mailing.forms import ReceiverForm, MessageForm
from mailing.models import Receiver, Message


class HomeTemplateView(TemplateView):
    """ Home template view """
    template_name = "mailing/home.html"


class ReceiverDetailView(DetailView):
    """Receiver detail view """
    model = Receiver
    form_class = ReceiverForm


class ReceiverCreateView(CreateView):
    """Receiver create view """
    model = Receiver
    form_class = ReceiverForm
    extra_context = {'title': 'Add your Client'}
    success_url = reverse_lazy('mailing:home_template')


class ReceiverUpdateView(UpdateView):
    """Receiver update view """
    model = Receiver
    form_class = ReceiverForm
    extra_context = {'title': 'Edit info about your Client'}
    success_url = reverse_lazy('mailing:home_template')


class ReceiverDeleteView(DeleteView):
    model = Receiver
    success_url = reverse_lazy("catalog:products_list")











class MessageDetailView(DetailView):
    """Messaage detail view """
    model = Message
    form_class = MessageForm


class MessageCreateView(CreateView):
    """Message create view """
    model = Message
    form_class = MessageForm
    extra_context = {'title': 'Add your message'}
    success_url = reverse_lazy('mailing:home_template')


class MessageUpdateView(UpdateView):
    """Message update view """
    model = Message
    form_class = MessageForm
    extra_context = {'title': 'Edit message'}
    success_url = reverse_lazy('mailing:home_template')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:home_template')