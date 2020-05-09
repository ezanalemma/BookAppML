from django.shortcuts import render
from polls.models import Book
import random
# Create your views here.
# def index(request):
# 	return render(request, 'home/index.html')

def index(request):
	# random.seed(1)
	book = random.choice(Book.objects.all())
	pk = book.book_id 
	bookPk = (Book.objects.get(pk=pk)).image_url
	# bookPkUrl = bookPK.get('small_image_url')
	return render(request, 'home/index.html', {'theSrc': bookPk})