import datetime

import requests
from dataclasses import fields
from smtplib import SMTPResponseException, SMTPRecipientsRefused, SMTPException

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from requests import Response

from config.settings import EMAIL_HOST_USER
from mailing.forms import ReceiverForm, MessageForm, MailingForm, AttemptForm
from mailing.models import Receiver, Message, Mailing, Attempt
from users.models import User


class HomeTemplateView(TemplateView):
    """ Home template view """
    template_name = "mailing/home.html"

class ReceiversListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """ Class for viewing all users. Authorization for moderators"""
    model = Receiver
    permission_required = 'mailing.view_all_receivers'



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

    def form_valid(self, form):
        form.instance.receiver_adder = self.request.user
        return super().form_valid(form)


class ReceiverUpdateView(UpdateView):
    """Receiver update view """
    model = Receiver
    form_class = ReceiverForm
    extra_context = {'title': 'Edit info about your Client'}
    success_url = reverse_lazy('mailing:home_template')

    # Adding logic to update Mailing only for user
    def get_form_class(self):
        user = self.request.user
        if user == self.object.receiver_adder:
            return MailingForm
        raise PermissionDenied


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



class StatisticsTemplateView(TemplateView):
    """ StatisticsPage template view """
    template_name = "mailing/statistics.html"

    def get(self, request, *args, **kwargs):
        user = self.request.user # get user
        mailiing_list = Mailing.objects.filter(mailing_sender=user)
        receivers_list = Receiver.objects.filter(receiver_adder=user)
        attempts_list = Attempt.objects.filter(attempt_sender=user)
        context = self.get_context_data(**kwargs)
        context['mailing_list'] = mailiing_list
        context['receivers_list'] = receivers_list
        context['attempts_list'] = attempts_list
        return self.render_to_response(context)


class MailingListView(LoginRequiredMixin, ListView):
    """ Class to get list of Mailings """
    model = Mailing

    def get(self, request, *args, **kwargs):

        # rendering all Mailing list for moderators
        if request.user.has_perm('mailing.view_all_mailings'):
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            return self.render_to_response(context)

        # rendering Mailing list for particular user
        else:
            self.object_list = self.get_queryset()
            user = self.request.user
            self.object_list = self.object_list.filter(mailing_sender=user)
            context = self.get_context_data()
            return self.render_to_response(context)


class MailingDeactivateView(LoginRequiredMixin, View):
    """ Change status of the Mailing to Draft for moderators"""

    def post(self, request, pk):
        mailing = get_object_or_404(Mailing, pk=pk)

        if not request.user.has_perm("mailing.deactivate_mailings"):
            return HttpResponseForbidden(
                "You do not have permission to change a status of the Mailing"
            )

        mailing.status = 'Created'
        mailing.save()

        return redirect("mailing:mailing_list")



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

    def form_valid(self, form):
        form.instance.mailing_sender = self.request.user
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    """Mailing update view """
    model = Mailing
    form_class = MailingForm
    extra_context = {'title': 'Edit Mailing'}
    success_url = reverse_lazy('mailing:home_template')

    # Adding logic to update Mailing only for user
    def get_form_class(self):
        user = self.request.user
        if user == self.object.mailing_sender:
            return MailingForm
        raise PermissionDenied


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:home_template')
    
    def post(self, request, *args, **kwargs):
        user = self.request.user
        self.object = self.get_object()
        if user == self.object.mailing_sender:
            return super().post(request, *args, **kwargs)
        raise PermissionDenied
    
    
    
    
    
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
        form.instance.attempt_sender = self.request.user
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