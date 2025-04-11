from django.core.cache import cache
from django.core.mail import send_mail

from config.settings import CACHE_ENABLED, EMAIL_HOST_USER
from mailing.models import Mailing, Message, Receiver


def get_messages_from_cache(user):
    """Get data for the messages from cache. If no data in cache, cache messages"""
    if not CACHE_ENABLED:
        return Message.objects.filter(message_sender=user)
    key = "message_list"
    messages = cache.get(key)
    if messages is not None:
        return messages
    message_list = Message.objects.filter(message_sender=user)
    cache.set(key, message_list)
    return message_list


def get_mailings_from_cache(user):
    """Get data for the mailings from cache. If no data in cache, cache mailings"""
    if not CACHE_ENABLED:
        return Mailing.objects.filter(mailing_sender=user)
    key = "mailing_list"
    mailings = cache.get(key)
    if mailings is not None:
        return mailings
    mailing_list = Mailing.objects.filter(mailing_sender=user)
    cache.set(key, mailing_list)
    return mailing_list


def get_receivers_from_cache(user):
    """Get data for the receivers from cache. If no data in cache, cache receivers"""
    if not CACHE_ENABLED:
        return Receiver.objects.filter(receiver_adder=user)
    key = "receiver_list"
    receivers = cache.get(key)
    if receivers is not None:
        return receivers
    receiver_list = Receiver.objects.filter(receiver_adder=user)
    cache.set(key, receiver_list)
    return receiver_list


def send_mailing(user_mail, subject, message):
    from_email = EMAIL_HOST_USER
    recipient_list = user_mail
    send_mail(subject, message, from_email, recipient_list)