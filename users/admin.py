from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdminModel(admin.ModelAdmin):
    readonly_fields = ['password', 'last_login', 'date_joined']
