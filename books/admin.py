from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Books, Category


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Books)
admin.site.register(Category)
# admin.site.register(Author)
