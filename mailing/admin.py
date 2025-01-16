from django.contrib import admin

from .models import Receiver, Message

#Register admin for Receiver model
@admin.register(Receiver)
class ReceiverAdmin(admin.ModelAdmin):
    list_display = ("name", "mail",)
    list_filter = ('name', 'mail',)
    search_fields = ('name', 'mail',)


#Register admin for Message model
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("title", "message",)
    list_filter = ('title', )
    search_fields = ('title', 'message',)