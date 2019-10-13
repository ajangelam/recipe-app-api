from core import models

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']

    # Field sets for edit user page.
    fieldsets = (
        (
            None,
            {'fields': ('email', 'password')}
        ),
        (
            _('Personal Information'),
            {'fields': ('name',)}
        ),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (
            _('Important dates'),
            {'fields': ('last_login',)}
        )
    )

    # Field sets for add user page.
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )


# Register User Admin class to User Model
admin.site.register(models.User, UserAdmin)
