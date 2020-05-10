from django.contrib import admin

# Register your models here.
from .models import UserBook

admin.site.register(UserBook)