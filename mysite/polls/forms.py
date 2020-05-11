from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import Question, Choice

Choices=(
	("1", "Art"),
	("2", "Biography"),
	("3", "Business"),
	("4", "Classics"),
	("5", "Crime"),
	("6", "Fantasy"),
	("7", "Fiction"),
	("8", "Horror"),
	("9", "Humor"),
	("10", "Mystery"),
	("11", "Non-Fiction"),
	("12", "Romance"),
	("13", "Suspense"),
	("14", "Sports"),
	("15", "Young Adult")


)

R=(
	("1", "Every Day"),
	("2", "Every other day"),
	("3", "Once a week"),
	("4", "Couple times a month")
)

Stars=(
	("1", "1 Star"),
	("2", "2 Stars"),
	("3", "3 Stars"),
	("4", "4 Stars"),
	("5", "5 Stars")
)

class SurveyForm(forms.Form):
	user = forms.CharField(label="Name ", max_length=100)
	genres = forms.MultipleChoiceField(label = "What are your favorite genres? " ,choices = Choices)
	average_read_time = forms.MultipleChoiceField(label = "How often do you read?", choices = R)
	last_book = forms.CharField(label="What is the last book you read? ", max_length=100)
	rating = forms.MultipleChoiceField(label = "How would you rate that book?",choices = Stars )
	favorite_author = forms.CharField(label = "Who is your favorite author", max_length=100)


        