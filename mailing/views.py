import datetime

import requests
from dataclasses import fields
from smtplib import SMTPResponseException, SMTPRecipientsRefused, SMTPException

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from requests import Response

from config.settings import EMAIL_HOST_USER
from mailing.forms import ReceiverForm, MessageForm, MailingForm, AttemptForm
from mailing.models import Receiver, Message, Mailing, Attempt


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


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Mailing create view """
    model = Mailing
    form_class = MailingForm
    extra_context = {'title': 'Add your mailing'}
    success_url = reverse_lazy('mailing:home_template')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        message = Message.objects.filter(message_chosen=True)
        context['mailing_message'] = message[0].message
        print(context)

        return context

    # def get(self, request, *args, **kwargs):
    #     message = Message.objects.filter(message_chosen=True)
    #     context = super().get_context_data(**kwargs)
    #     category_id = self.object.id
    #     context['category_name'] = self.object.category_name
    #
    #     return super().get(request, *args, **kwargs)


class MailingUpdateView(UpdateView):
    """Mailing update view """
    model = Mailing
    form_class = MailingForm
    extra_context = {'title': 'Edit Mailing'}
    success_url = reverse_lazy('mailing:home_template')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:home_template')
    
    
    
    
    
    
    
class AttemptDetailView(DetailView):
    """Attempt detail view """
    model = Attempt
    form_class = AttemptForm


class AttemptCreateView(CreateView):
    """Attempt create view """
    model = Attempt
    form_class = AttemptForm
    extra_context = {'title': 'Add your Attempt'}
    success_url = reverse_lazy('mailing:home_template')



    def form_valid(self, form):
        """ Sending mails logic during creating a new attempt"""
        mailing = form.save()
        users = mailing.mailing.receivers.all()
        user_mail =[]
        for user in users:
            user_mail.append(user.email)
        try:
            self.send_mailing(user_mail)
            mailing.mailing.status = 'Launched'
            mailing.mailing.save()
            mailing.attempt_status = 'Succeed'
            mailing.server_respond = 'All mailings are done'
        except Exception as e:
            mailing.server_respond = e
            mailing.attempt_status = 'Not Succeed'
        mailing.save()
        end_time = datetime.datetime.now()
        mailing.mailing.end_sending = end_time
        mailing.mailing.status = 'Completed'
        mailing.mailing.save()
        return super().form_valid(form)

    def send_mailing(self, user_mail):
        subject = 'Welcome Trial!'
        message = 'Hello  TRIAL'
        from_email = EMAIL_HOST_USER
        recipient_list = user_mail
        send_mail(subject, message, from_email, recipient_list)


class AttemptUpdateView(UpdateView):
    """Attempt update view """
    model = Attempt
    form_class = AttemptForm
    extra_context = {'title': 'Edit Attempt'}
    success_url = reverse_lazy('mailing:home_template')


class AttemptDeleteView(DeleteView):
    model = Attempt
    success_url = reverse_lazy('mailing:home_template')