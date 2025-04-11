from django.contrib import admin

from .models import User


# Register admin for Receiver model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Registering User in Admin"""

    list_display = (
        "is_active",
        "password",
        "email",
        "name",
        "last_name",
        "phone_number",
        "avatar",
    )
    list_filter = (
        "last_name",
        "email",
    )
    search_fields = (
        "last_name",
        "email",
    )
