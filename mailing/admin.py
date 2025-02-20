from django.contrib import admin

from .models import Receiver, Message, Mailing, Attempt


# Register admin for Receiver model
@admin.register(Receiver)
class ReceiverAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
    )
    list_filter = (
        "name",
        "email",
    )
    search_fields = (
        "name",
        "email",
    )


# Register admin for Message model
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "message",
    )
    list_filter = ("title",)
    search_fields = (
        "title",
        "message",
    )


# Register admin for Mailing model
@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = (
        "first_sending",
        "end_sending",
        "status",
        "receivers__name",
        "message__title",
    )
    list_filter = ("status",)
    search_fields = (
        "status",
        "receivers__name",
    )


# Register admin for Attempt model
@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = (
        "attempt_time",
        "attempt_status",
        "server_respond",
    )
    list_filter = ("attempt_status",)
    search_fields = (
        "attempt_status",
        "server_respond",
    )
