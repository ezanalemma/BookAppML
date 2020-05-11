from django.db import models

# Create your models here.
class UserBook(models.Model):
	username = models.CharField(max_length=30, primary_key=True)
	book_id = models.IntegerField(default=0)

class BooksRead(models.Model):
	username = models.CharField(default=0, primary_key=True, max_length=30)
	book_id = models.IntegerField(default=0)