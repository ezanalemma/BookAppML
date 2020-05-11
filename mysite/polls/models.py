import datetime

from django.db import models
from django.utils import timezone
from .forms import SurveyForm


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
    	return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.BooleanField()
    complete = models.BooleanField();
    def __str__(self):
    	return self.choice_text


class Book(models.Model):
    book_id = models.IntegerField(default=0, primary_key=True);
    good_reads_id = models.IntegerField(default=0);
    title = models.CharField(default = 0,max_length=200);
    authors = models.CharField(default = 0, max_length=300);
    year = models.FloatField(default=0);
    genre = models.CharField(max_length= 200);
    tag_id = models.IntegerField(default=0);
    image_url  = models.URLField(blank=True, null=True)
    small_image_url = models.URLField(blank=True, null=True);
    #	book_count = IntegerField();
    isbn = models.CharField(default=0, max_length=200);
    isbn13 = models.CharField(default=0, max_length=200);
    def __str__(self):
        return self.title
    def get_image(self):
        return self.image_url;

class Rating(models.Model):
    user_id = models.IntegerField(default=0)
    book_id = models.IntegerField(default =0)
    rating = models.IntegerField(default=0)

class Survey(models.Model):
    username = models.CharField(max_length=100)
    genres = models.CharField(max_length = 100)
    average_read_time = models.CharField(max_length=100)
    last_book = models.CharField(max_length=100)
    rating = models.CharField(max_length=100 )
    favorite_author = models.CharField(max_length=100)
    def __str__(self):
        return self.username


class UserSurvey(models.Model):
    username = models.CharField(max_length =50, primary_key=True)
    survey_results = models.ForeignKey(Survey, on_delete=models.CASCADE)
	