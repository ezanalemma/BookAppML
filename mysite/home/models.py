from django.db import models

# Create your models here.
class UserBook(models.Model):
	username = models.CharField(max_length=30, primary_key=True)
	book_id = models.IntegerField(default=0)