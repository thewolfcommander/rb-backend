from django.contrib import admin
from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ['email', 'mobile_number', 'full_name', 'gender']