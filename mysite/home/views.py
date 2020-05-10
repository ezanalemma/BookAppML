# from django.shortcuts import render
# from polls.models import Book
# import random
# # Create your views here.
# # def index(request):
# # 	return render(request, 'home/index.html')

# def index(request):
# 	# random.seed(1)
# 	book = random.choice(Book.objects.all())
# 	pk = book.book_id 
# 	bookPk = (Book.objects.get(pk=pk)).image_url
# 	# bookPkUrl = bookPK.get('small_image_url')
# 	return render(request, 'home/index.html', {'theSrc': bookPk})



from django.shortcuts import render
from polls.models import Book
from .models import UserBook
import random
# Create your views here.
def index(request):
	user1 = request.user
	num_results = UserBook.objects.filter(username=user1.username).count()
	# obj = UserBook.objects.get(pk=pk)
	if num_results > 0:
		obj = UserBook.objects.get(pk=user1.username)
		pk1 = obj.book_id
		bookPk = (Book.objects.get(pk=pk1)).image_url
		# site = "home/" + pk + "/index.html"
		# return render(request, site, {'theSrc': bookPk})

	else:
		book = random.choice(Book.objects.all())
		pk1 = book.book_id 
		bookPk = (Book.objects.get(pk=pk1)).image_url
		UserBook.objects.create(username=user1.username, book_id=pk1)



	# for book in UserBook.objects.all():
	# 	if book.username == pk:
	# 		pk1 = book.book_id 
	# 		bookPk = (Book.objects.get(pk=pk1)).image_url
	# 		return render(request, 'home/index.html', {'theSrc': bookPk})
	return render(request, 'home/index.html', {'theSrc': bookPk})
	# site = "home/" + pk + "/index.html"
	# return render(request, site, {'theSrc': bookPk})

def detail(request):
	# random.seed(1)
	user1 = request.user #get current user
	book = random.choice(Book.objects.all()) 
	pk1 = book.book_id 
	bookPk = (Book.objects.get(pk=pk1)).image_url
	# num_results = UserBook.objects.filter(username=user1.username).count()
	# if num_results > 0:
	user_book = UserBook.objects.get(pk=user1.username)
	user_book.book_id = pk1
	user_book.save()

	# else:
	# 	user_book = UserBook.objects.create(username=username, book_id=pk1)
	
	return render(request, 'home/index.html', {'theSrc': bookPk})

	# bookPkUrl = bookPK.get('small_image_url')
	# return render(request, 'home/index.html')
	# site = "home/" + pk + "/index.html"
	# return render(request, site, {'theSrc': bookPk})

