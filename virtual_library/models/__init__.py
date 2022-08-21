# import all models to this module
from .user import User
from .category import Category
from .book import Book


# register to admin site
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# admin.site.register(User)
admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Book)