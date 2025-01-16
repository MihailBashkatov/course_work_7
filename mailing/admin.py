from django.contrib import admin

from .models import Receiver

#Register admin for Receiver model
@admin.register(Receiver)
class ReceiverAdmin(admin.ModelAdmin):
    list_display = ("name", "mail",)
    list_filter = ('name', 'mail',)
    search_fields = ('name', 'mail',)


