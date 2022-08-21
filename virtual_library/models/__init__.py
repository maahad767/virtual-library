# import all models to this module
from .user import *
from .category import *
from .book import *
from .order import *
from .rating import *

# register to admin site
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'photo')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone', 'address')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Rating)
admin.site.register(RentOrder)
