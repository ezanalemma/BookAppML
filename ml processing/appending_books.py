#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:59:41 2020

@author: ezana
"""

import pandas as pd
import matplotlib.pyplot as plt
import collections
#import plotly.express as px

import sklearn_recommender as skr
#import ask_watson as ask


#GET NECESSARY INPUT FILES SO 3 CSVs, BOOKS.CSV, BOOK_TAGS.CSV, TAGS.CSV
books = pd.read_csv("books.csv")
tags = pd.read_csv("book_tags.csv")
tag_names = pd.read_csv("tags.csv")
tag_2 = pd.read_csv("tags-2.csv")

#CREATE OTHER CSV FOR MERGING TWO AT A TIME
tags_with_names = pd.read_csv("book_tags_with_names.csv")

current_books_with_tags = pd.read_csv("books_with_tag_names.csv")

single_tags_cleaned = pd.read_csv("single_tags_cleaned.csv")

single_tags_with_names = pd.read_csv("single_tags_with_names.csv")

books_clean = pd.read_csv("books_clean.csv")

books_clean_filled = pd.read_csv("books_clean_filled.csv")

ratings_genres = pd.read_csv("ratings_genres.csv")

user_genre_average_rating = pd.read_csv("user_genre_average_rating.csv")

#THESE MERGES WERE NEEDED FOR INCREMENTALLY GETTING TO THE DATASET WE NEEDED

#merging the tags directly to books we had with their goodreads ID
#merged = tags.merge(books, on='goodreads_book_id')
#merged.to_csv("output2.csv", index=False)

#merging the tags (#) with their tag names (genre)
#tags_with_names = tags.merge(tag_names, on='tag_id')
#tags_with_names.to_csv("book_tags_with_names.csv", index=False)

#merging the tag names to all books we had
#books_with_tag_names = books.merge(tags_with_names, on='goodreads_book_id')
#books_with_tag_names.to_csv("books_with_tag_names.csv", index=False)

#ISSUE with the amount of irrelevant tags for each book. 

#visualizing our data to understand how the genres are composed and how we can apply it in project
#book = current_books_with_tags.columns.str.strip('goodreads_book_id')
#tag = current_books_with_tags.columns.str.strip('tag_name')
#fig = px.line(current_books_with_tags, x = 'goodreads_book_id', y = 'tag_name', title='Books with their genres.')
#fig.show()
#current_books_with_tags.plot()



#THESE SEEM TO BE THE PRINCIPAL GENRES IN OUR DATASET

#tag_2.filter(like=["art", "biography", "business", "chick lit", "children's", "christian", "classics", "comics", "contemporary", "cookbooks", "crime", "ebooks", "fantasy", "fiction", "gay and lesbian", "graphic novels", "historical fiction", "history", "horror", "humor and comedy", "manga", "memoir", "music", "mystery", "nonfiction", "paranormal", "philosophy", "poetry", "psychology", "religion", "romance", "science", "science fiction", "self help", "suspense", "spirituality", "sports", "thriller", "travel", "young adult"], axis=0)
#print(tag_2[tag_2['tag_name'].isin(["art", "biography", "business", "chick lit", "children's", "christian", "classics", "comics", "contemporary", "cookbooks", "crime", "ebooks", "fantasy", "fiction", "gay and lesbian", "graphic novels", "historical fiction", "history", "horror", "humor and comedy", "manga", "memoir", "music", "mystery", "nonfiction", "paranormal", "philosophy", "poetry", "psychology", "religion", "romance", "science", "science fiction", "self help", "suspense", "spirituality", "sports", "thriller", "travel", "young adult"])])
cleaned_tags = tag_2[tag_2['tag_name'].isin(["art", "biography", "business", "chick lit", "children's", "christian", "classics", "comics", "contemporary", "cookbooks", "crime", "ebooks", "fantasy", "fiction", "gay and lesbian", "graphic novels", "historical fiction", "history", "horror", "humor and comedy", "manga", "memoir", "music", "mystery", "nonfiction", "paranormal", "philosophy", "poetry", "psychology", "religion", "romance", "science", "science fiction", "self help", "suspense", "spirituality", "sports", "thriller", "travel", "young adult"])]
#cleaned_tags.to_csv("tags_cleaned.csv", index = False)
#print(cleaned_tags.tag_id.unique())

#the tags that correspond to the principal genres
tags_id_cleaned = [ 2938,  4605,  5951,  7077,  7457,  7778,  8055,  8150,  8517, 10210, 11305, 11743, 14552, 14821, 19052, 19733, 20673, 20939, 21773, 22973, 23471, 23831, 24526, 25647, 26138, 26816, 28384, 28422, 29076, 30358, 31155]

#the bookIDs with their tags out of the principal genres
cleaned_book_tags = tags[tags['tag_id'].isin(tags_id_cleaned)]
#print("books with their all genres each.")
#print(cleaned_book_tags.head(20))

#take the most relevant one for each bookID!
cleaned_random_book_tags = cleaned_book_tags.groupby('goodreads_book_id').apply(lambda x: x.sample(1)).reset_index(drop=True)
print("pick most relevant one for each bookID")
print(cleaned_random_book_tags.head(20))

#make sure no book is left out by comparing the amount of rows for "books.csv"  and cleaned_random_book_tags
print(cleaned_random_book_tags.shape)
print(books.shape)

#cleaned_random_book_tags.to_csv("single_tags_cleaned.csv", index = False)

#add names to the tags again now that one book has one major genre
#single_tags_with_names = single_tags_cleaned.merge(tag_names, on='tag_id')
#print(single_tags_with_names)
#single_tags_with_names.to_csv("single_tags_with_names.csv", index = False)


books_with_cleaned_single_tags = books.merge(single_tags_with_names, on='goodreads_book_id')

print("The books with one genre each.")
print(books_with_cleaned_single_tags.head(20))
#books_with_cleaned_single_tags.to_csv("books_with_single_tags.csv", index = False)


books_with_cleaned_single_tags = books_with_cleaned_single_tags.drop(["count", "work_id", "language_code", "work_text_reviews_count", "work_ratings_count", "ratings_1", "ratings_2", "ratings_3", "ratings_4", "ratings_5", "average_rating", "ratings_count", "books_count", "title", "best_book_id"], axis=1)
books_with_cleaned_single_tags = books_with_cleaned_single_tags.rename(columns={"original_publication_year": "year", "original_title": "title", "tag_name": "genre"})
books_with_cleaned_single_tags = books_with_cleaned_single_tags[['book_id', 'goodreads_book_id', 'title', 'authors', 'year', 'genre', 'tag_id', 'image_url', 'small_image_url', 'isbn', 'isbn13' ]]
print("renamed and ordered dataset to final version.")
print(books_with_cleaned_single_tags.head(20))

#outputting final version
#books_with_cleaned_single_tags.to_csv("books_clean.csv", index = False)


#Fill all empty years to get a working dataset
#books_clean['year'].fillna(2000.0, inplace=True)
#books_clean.to_csv("books_clean_filled.csv", index = False)


#PLOTS FOR PRESENTATION
book = books_clean_filled.columns.str.strip('goodreads_book_id')
tag = books_clean_filled.columns.str.strip('genre')

df = pd.DataFrame(books_clean_filled)

l = df.genre
count_genre = collections.Counter(l)
plt.bar(list(count_genre.keys()), list(count_genre.values()))
plt.xticks(rotation=90)
plt.suptitle('Genres in Our Dataset')
plt.xlabel('Genre')
plt.ylabel('Number of Books')

plt.show()

l2 = df.year
count_year = collections.Counter(l2)
plt.bar(list(count_year.keys()), list(count_year.values()))
plt.xlim(1750, 2020)
plt.suptitle('Distribution of Publication Year in Our Dataset')
plt.xlabel('Publication Year')
plt.ylabel('Number of Books')

plt.show()

listOfSeries = [pd.Series([7130, 405.0, 'contemporary', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7131, 405.0, 'fiction', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7132, 405.0, 'mystery', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7133, 405.0, 'romance', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7134, 405.0, 'history', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7135, 405.0, 'ebooks', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7136, 405.0, 'fantasy', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7137, 405.0, 'memoir', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7138, 405.0, 'thriller', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7139, 405.0, 'paranormal', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7140, 405.0, 'classics', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7141, 405.0, 'horror', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7142, 405.0, 'nonfiction', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7143, 405.0, 'crime', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7144, 405.0, 'religion', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7145, 405.0, 'science', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7146, 405.0, 'biography', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7147, 405.0, 'art', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7148, 405.0, 'travel', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7149, 405.0, 'psychology', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7150, 405.0, 'music', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7151, 405.0, 'philosophy', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7152, 405.0, 'suspense', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7153, 405.0, 'comics', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7154, 405.0, 'spirituality', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7155, 405.0, 'christian', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7156, 405.0, 'poetry', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7157, 405.0, 'manga', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7158, 405.0, 'business', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7159, 405.0, 'cookbooks', 2.5], index=user_genre_average_rating.columns ) ,
                pd.Series([7160, 405.0, 'sports', 2.5], index=user_genre_average_rating.columns )]

with_user_input = user_genre_average_rating.append(listOfSeries , ignore_index=True)

#before user input
#print(user_genre_average_rating)
#after user input
#print(with_user_input)

#verify how many genres we're working with #31
#print(df['genre'].unique())

#print(ratings_genres.head(20))

#most similar user

print("INPUT: user2. OUTPUT: most similar users in order to suggest book.\n")

#organizing dataset to make it ingestible
tf = skr.transformer.UserItemTransformer(user_col='user_id', item_col='genre', value_col='rating', binarize=False)
user_item = tf.transform(with_user_input)
print(user_item) #user_item matrix 



#print(updated_user_item)

#tests
print("\ntests:")
print("amount of users: " + str(user_item.shape[0]) )
print("amount of genres per user: " + str(user_item.shape[1]) )
print("average amount of total stars from a user:" + str(user_item.sum(axis=1)[1]) )

# computing similarity of the input user to users in dataset
tf = skr.transformer.SimilarityTransformer(cols=(0, -1), normalize=False)
sim = tf.transform(user_item)

# get list of most similar ids
rec = skr.recommender.SimilarityRecommender(None).fit(sim)
most_similar_users = rec.predict([405])[0]

print("\n5 most similar users list: ")
print(most_similar_users[:5])

#user_genre_average_rating

#print(user_item.loc[[405, 284]])
#printable = user_item.loc[[405, 284]]
#printable.to_csv("thetwochosen.csv", index = False)


