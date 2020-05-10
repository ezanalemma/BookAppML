from django.shortcuts import render
from polls.models import Book
from .models import UserBook
import random

# Create your views here.

def index(request):
	user1 = request.user
	num_results = UserBook.objects.filter(username=user1.username).count()
	if num_results > 0:
		obj = UserBook.objects.get(pk=user1.username)
		pk1 = obj.book_id
		bookPk = (Book.objects.get(pk=pk1)).image_url

	else:
		book = random.choice(Book.objects.all())
		pk1 = book.book_id 
		bookPk = (Book.objects.get(pk=pk1)).image_url
		UserBook.objects.create(username=user1.username, book_id=pk1)

	return render(request, 'home/index2.html', {'theSrc': bookPk})

def index2(request):
	# random.seed(1)
	user1 = request.user #get current user
	book = random.choice(Book.objects.all()) 
	pk1 = book.book_id 
	bookPk = (Book.objects.get(pk=pk1)).image_url

	user_book = UserBook.objects.get(pk=user1.username)
	user_book.book_id = pk1
	user_book.save()

	return render(request, 'home/index2.html', {'theSrc': bookPk})

