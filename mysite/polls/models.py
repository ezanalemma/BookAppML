import datetime

from django.db import models
from django.utils import timezone


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
    votes = models.IntegerField(default=0)
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
    user_id = models.IntegerField(default=0);
    art =  models.IntegerField(default=0);
    biography =  models.IntegerField(default=0);
    business =  models.IntegerField(default=0);
    chick_lit =  models.IntegerField(default=0);
    childrens =  models.IntegerField(default=0);
    chritstian =  models.IntegerField(default=0);
    classics =  models.IntegerField(default=0);
    comics =  models.IntegerField(default=0);
    contemporary =  models.IntegerField(default=0);
    cookbooks =  models.IntegerField(default=0);
    crime =  models.IntegerField(default=0);
    ebooks =  models.IntegerField(default=0);
    fantasy =  models.IntegerField(default=0);
    fiction =  models.IntegerField(default=0);
    gay_lesbian =  models.IntegerField(default=0);
    graphic_novels =  models.IntegerField(default=0);
    historical_fiction =  models.IntegerField(default=0);
    history =  models.IntegerField(default=0);
    horror =  models.IntegerField(default=0);
    humor =  models.IntegerField(default=0);
    manga =  models.IntegerField(default=0);
    memoir =  models.IntegerField(default=0);
    music =  models.IntegerField(default=0);
    mystery =  models.IntegerField(default=0);
    nonfiction =  models.IntegerField(default=0);
    paranormal =  models.IntegerField(default=0);
    philosophy =  models.IntegerField(default=0);
    poetry =  models.IntegerField(default=0);
    psychology =  models.IntegerField(default=0);
    religion =  models.IntegerField(default=0);
    romance =  models.IntegerField(default=0);
    science =  models.IntegerField(default=0);
    science_fiction =  models.IntegerField(default=0);
    self_help =  models.IntegerField(default=0);
    suspense =  models.IntegerField(default=0);
    spirituality =  models.IntegerField(default=0);
    sports =  models.IntegerField(default=0);
    thriller =  models.IntegerField(default=0);
    travel =  models.IntegerField(default=0);
    young_adult =  models.IntegerField(default=0);

	