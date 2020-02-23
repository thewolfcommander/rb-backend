from django.contrib import admin

from .models import (
    Contact,
)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'full_name', 'email', 'enquiry_choice', 'ip_address']
    list_filter = ['timestamp', 'enquiry_choice']