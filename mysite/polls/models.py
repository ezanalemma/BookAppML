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

#class MyCSvModel(CsvModel):
#	bookID = IntegerField();
#	good_reads_id = IntegerField();
#	best_book_id = IntegerField();
#	work_id = IntegerField();
#	book_count = IntegerField();
#	ISBN = FloatField();
#	ISBN13 = FloatField();
#	authors = CharField();
#	original_publication_year = IntegerField();
#	original_title = CharField();
#	title = CharField();
#	language_code = CharField();
#	ratings_count = IntegerField();
#	work_ratings_count = IntegerField();
#	work_text_reviews_count = IntegerField();
#	ratings_1 = IntegerField();
#	ratings_2 = IntegerField();
#	ratings_3 = IntegerField();
#	ratings_4 = IntegerField();
#	ratings_5 = IntegerField();
#	image_url  = CharField();
#	small_image_url = CharField();
#	tag_id = IntegerField();
#	count = IntegerField();
#	tag_name = CharField();


















	
    	
    


