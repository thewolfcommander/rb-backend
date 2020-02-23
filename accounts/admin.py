from django.contrib import admin
from .models import (
    User,
    CustomUserPermissions,
    UserType,
    UserProfile,
    UserDevice
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    actions = ['make_user_active', 'make_user_inactive', 'make_user_staff', 'make_user_non_staff']


    def make_user_active(self, request, queryset):
        """
        Make multiple user active
        """
        rows_updated = queryset.update(is_active=True)
        if rows_updated == 1:
            message_bit = "1 user was"
        else:
            message_bit = "{} users were".format(rows_updated)
        self.message_user(request, "{} successfully marked as active.".format(message_bit))
    make_user_active.short_description = "Make selected users active"

    def make_user_inactive(self, request, queryset):
        """
        Make multiple user inactive
        """
        rows_updated = queryset.update(is_active=False)
        if rows_updated == 1:
            message_bit = "1 user was"
        else:
            message_bit = "{} users were".format(rows_updated)
        self.message_user(request, "{} successfully marked as inactive.".format(message_bit))
    make_user_inactive.short_description = "Make selected users Inactive"

    def make_user_staff(self, request, queryset):
        """
        Make multiple user staff
        """
        rows_updated = queryset.update(is_staff=True)
        if rows_updated == 1:
            message_bit = "1 user was"
        else:
            message_bit = "{} users were".format(rows_updated)
        self.message_user(request, "{} successfully marked as staff.".format(message_bit))
    make_user_staff.short_description = "Make selected users Staff"

    def make_user_non_staff(self, request, queryset):
        """
        Make multiple user non staff
        """
        rows_updated = queryset.update(is_staff=False)
        if rows_updated == 1:
            message_bit = "1 user was"
        else:
            message_bit = "{} users were".format(rows_updated)
        self.message_user(request, "{} successfully marked as staff.".format(message_bit))
    make_user_non_staff.short_description = "Make selected users non Staff"


@admin.register(CustomUserPermissions)
class CustomUserPermissionsAdmin(admin.ModelAdmin):
    list_display = ['name', 'priority']


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'priority']
    list_filter = ['priority']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'mobile', 'user_type', 'timestamp']
    list_filter = ['timestamp', 'user_type']


@admin.register(UserDevice)
class UserDeviceAdmin(admin.ModelAdmin):
    list_display = ['user', 'device_name', 'os', 'browser', 'ip_address', 'timestamp']
    list_filter = ['os', 'browser', 'timestamp']