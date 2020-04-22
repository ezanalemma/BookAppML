import datetime

from django.db import models
from django.utils import timezone
#from adaptor.model import CsvModel

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
    def __str__(self):
    	return self.choice_text


class Rating(models.Model):
	#listing = models.ForeignKey(listing)
	#user = models.ForeignKey(settings.AUTH_USER_MODEL)
	#dif_rate = models.IntegerField(null=True, blank=True)
	#other_rate = models.IntegerField(null=True, blank=True)
	rating_text = models.CharField(max_length=300, unique=True)
	rating = models.IntegerField(default=0)
	#book = MyCSvModel.title
	def __str__(self):
		return self.rating_text

class Book(models.Model):
	book_id = models.IntegerField();
	good_reads_id = models.IntegerField();
	title = models.CharField(max_length=200);
	authors = models.CharField(max_length=300);
	year = models.IntegerField();
	genre = models.CharField(max_length= 200);
	tag_id = models.IntegerField();
	image_url  = models.CharField(max_length=300);
	small_image_url = models.CharField(max_length=300);
#	book_count = IntegerField();
	isbn = models.IntegerField();
	isbn13 = models.IntegerField();
	def __str__(self):
		return self.title
	def get_image(self):
		return self.image_url



















	
    	
    


