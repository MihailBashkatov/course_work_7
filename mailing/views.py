from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView

from mailing.forms import ReceiverForm, MessageForm, MailingForm
from mailing.models import Receiver, Message, Mailing


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









class MailingPageTemplateView(TemplateView):
    """ MailingPage template view """
    template_name = "mailing/mailing_page.html"

    def get(self, request, *args, **kwargs):
        messages_list = Message.objects.all()
        receivers_list = Receiver.objects.all()
        context = self.get_context_data(**kwargs)
        context['messages_list'] = messages_list
        context['receivers_list'] = receivers_list
        return self.render_to_response(context)



class ChosenMailingPageTemplateView(TemplateView):
    """ ChosenMailingPage template view """
    template_name = "mailing/chosen_list_for_mailing.html"

    def get(self, request, *args, **kwargs):
        messages_list = Message.objects.all()
        receivers_list = Receiver.objects.all()
        context = self.get_context_data(**kwargs)
        context['messages_list'] = messages_list
        context['receivers_list'] = receivers_list
        return self.render_to_response(context)



class ReceiverChosenView(View):
    """ Class to change if receiver chosen for mailing list """
    def post(self, request, pk):
        receiver = get_object_or_404(Receiver, pk=pk)
        if receiver.receiver_chosen:
            receiver.receiver_chosen = False

        elif not receiver.receiver_chosen:
            receiver.receiver_chosen = True
        receiver.save()

        return redirect("mailing:mailing_page_template")









class MailingDetailView(DetailView):
    """Mailing detail view """
    model = Mailing
    form_class = MailingForm


class MailingCreateView(CreateView):
    """Mailing create view """
    model = Mailing
    form_class = MailingForm
    extra_context = {'title': 'Add your mailing'}
    success_url = reverse_lazy('mailing:home_template')


class MailingUpdateView(UpdateView):
    """Mailing update view """
    model = Mailing
    form_class = MailingForm
    extra_context = {'title': 'Edit Mailing'}
    success_url = reverse_lazy('mailing:home_template')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:home_template')