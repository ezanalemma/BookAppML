from django.contrib import admin

# Register your models here.
from .models import UserBook
from .models import BooksRead

admin.site.register(UserBook)
# admin.site.register(BooksRead)
admin.site.register(BooksRead)