from django.contrib import admin

from .models import Attempt, Mailing, Message, Receiver


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
    list_display = ("title", "message", "message_chosen")
    list_editable = ("message_chosen",)
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
        "get_receivers",
        "message__title",
    )
    list_editable = ("status",)
    list_filter = ("status",)
    filter_horizontal = ["receivers"]
    search_fields = (
        "status",
        "receivers__name",
    )

    @admin.display(description="receivers")
    def get_receivers(self, obj):
        return [receiver.email for receiver in obj.receivers.all()]


# Register admin for Attempt model
@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = (
        "attempt_time",
        "attempt_status",
        "server_respond",
        "get_receivers",
        "mailing__message__title",
    )
    list_filter = ("attempt_status",)
    search_fields = (
        "attempt_status",
        "server_respond",
    )

    @admin.display(description="receivers")
    def get_receivers(self, obj):
        return [receiver.email for receiver in obj.mailing.receivers.all()]
