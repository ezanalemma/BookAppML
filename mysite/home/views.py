from django.shortcuts import render
from polls.models import Book, Rating
from .models import UserBook
import random
#import pandas as pd
#import collections
#import sklearn_recommender as skr

# Create your views here.

def index(request):
	user1 = request.user
	num_results = UserBook.objects.filter(username=user1.username).count()
	if num_results > 0:
		obj = UserBook.objects.get(pk=user1.username)
		pk1 = obj.book_id
		bookPk = (Book.objects.get(pk=pk1)).image_url

	else:
		# book = random.choice(Book.objects.all())
		# pk1 = book.book_id 
		pk1 = get_book_rec(user1)
		bookPk = (Book.objects.get(pk=pk1)).image_url
		UserBook.objects.create(username=user1.username, book_id=pk1)

	return render(request, 'home/index2.html', {'theSrc': bookPk})

def index2(request):
	# random.seed(1)
	user1 = request.user #get current user
	book = random.choice(Book.objects.all()) 
	pk1 = book.book_id 
	#REPLACE pk1 WITH get_book_rec(user1):
	# pk1 = get_book_rec(user1)
	bookPk = (Book.objects.get(pk=pk1)).image_url

	user_book = UserBook.objects.get(pk=user1.username)
	user_book.book_id = pk1
	user_book.save()

	return render(request, 'home/index2.html', {'theSrc': bookPk})


def get_book_rec(user):
	#user_genre_average_rating = pd.read_csv("/BookAppML/ml processing/user_genre_average_rating.csv")
	#tf = skr.transformer.UserItemTransformer(user_col='user_id', item_col='genre', value_col='rating', binarize=False)
	#user_item = tf.transform(user_genre_average_rating)
	#tf = skr.transformer.SimilarityTransformer(cols=(0, -1), normalize=False)
	#sim = tf.transform(user_item)
	#rec = skr.recommender.SimilarityRecommender(None).fit(sim)

	# 2 should be replaced with current logged in user's user_id with their survey preferences etc
	#most_similar_user = rec.predict([2])[0] 

	# FIX: get list not working
#	for obj in Rating.objects.getlist(pk=most_similar_user):
#		if obj.rating == 5:
#			return obj.book_id
	book = random.choice(Book.objects.all());
	pk1 = book.book_id 
	return pk1

