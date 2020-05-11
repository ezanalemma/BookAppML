from django.shortcuts import render
from polls.models import Book, Rating
from .models import UserBook, BooksRead
import random
import pandas as pd
import numpy as np
import collections
import sklearn_recommender as skr
from polls.models import Survey

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
	# book = random.choice(Book.objects.all()) 
	# pk1 = book.book_id 
	#REPLACE pk1 WITH get_book_rec(user1):
	pk1 = get_book_rec(user1)
	bookPk = (Book.objects.get(pk=pk1)).image_url

	user_book = UserBook.objects.get(pk=user1.username)
	user_book.book_id = pk1
	user_book.save()

	return render(request, 'home/index2.html', {'theSrc': bookPk})


def get_book_rec(user1):
	user_genre_average_rating = pd.read_csv("home/user_genre_average_rating.csv")

	listOfSeries = []
	# genre_num = 0
	survey_obj = None
	for survey in Survey.objects.all():
		if survey.username == user1.username:
			survey_obj = survey

	# genre_tup = Choices[genre_num - 1]
	# genre = genre_tup[1]

	allGenres = [
		'contemporary', 
		'fiction', 
		'mystery', 
		'romance', 
		'history', 
		'ebooks', 
		'fantasy',
		'memoir',
		'thriller', 
		'paranormal',
		'classics',
		'horror',
		'nonfiction',
		'crime',
		'religion',
		'science',
		'biography',
		'art',
		'travel',
		'psychology',
		'music',
		'philosophy',
		'suspense',
		'comics',
		'spirituality',
		'christian',
		'poetry',
		'manga',
		'business',
		'cookbooks',
		'sports'
	]

	for g in allGenres:
		if not(survey_obj is None):
			r = getattr(survey_obj, g, 2.5)
			s = pd.Series([7130, 405.0, g, r], index=user_genre_average_rating.columns ) 
		else:
			s = pd.Series([7130, 405.0, g, 2.5], index=user_genre_average_rating.columns )
		listOfSeries.append(s) 
	with_user_input = user_genre_average_rating.append(listOfSeries , ignore_index=True)
	tf = skr.transformer.UserItemTransformer(user_col='user_id', item_col='genre', value_col='rating', binarize=False)
	user_item = tf.transform(with_user_input)


	# tf = skr.transformer.UserItemTransformer(user_col='user_id', item_col='genre', value_col='rating', binarize=False)
	# user_item = tf.transform(user_genre_average_rating)
	tf = skr.transformer.SimilarityTransformer(cols=(0, -1), normalize=False)
	sim = tf.transform(user_item)
	rec = skr.recommender.SimilarityRecommender(None).fit(sim)

	# 2 should be replaced with current logged in user's user_id with their survey preferences etc
	most_similar_users = rec.predict([405])[0] 

	# books = Rating.objects.getlist(pk=most_similar_user)
	books = Rating.objects.filter(user_id=most_similar_users[0],rating=5)
	if books:
		for b in books:
			if BooksRead.objects.filter(username=user1.username, book_id=b.book_id).count() < 0:
				BooksRead.objects.create(username=user1.username, book_id=pk1)
				return b.book_id

	books = Rating.objects.filter(user_id=most_similar_users[0],rating=4)
	if books:
		for b in books:
			if BooksRead.objects.filter(username=user1.username, book_id=b.book_id).count() < 0:
				BooksRead.objects.create(username=user1.username, book_id=pk1)
				return b.book_id

	books = Rating.objects.filter(user_id=most_similar_users[0],rating=3)
	if books:
		for b in books:
			if BooksRead.objects.filter(username=user1.username, book_id=b.book_id).count() < 0:
				BooksRead.objects.create(username=user1.username, book_id=pk1)
				return b.book_id

	book = random.choice(Book.objects.all());
	pk1 = book.book_id 
	return pk1