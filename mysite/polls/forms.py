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
	# question = "What are you favorite genres? Options: Art, Biography, Business, Classics, Crime, Fantasy, Fiction, Horror, Humor, Mystery, Non-Fiction, Romance, Suspense, Sports, Young Adult"
	user = forms.CharField(label="Username", max_length=100)
	art = forms.IntegerField(label="Rate the genre (1-5): Art: ", min_value=1, max_value=5)
	bio = forms.IntegerField(label="Rate the genre (1-5): Biography: ", min_value=1, max_value=5)
	business = forms.IntegerField(label="Rate the genres (1-5): Business: ", min_value=1, max_value=5)
	classics = forms.IntegerField(label="Rate the genres (1-5): Classics: ", min_value=1, max_value=5)
	crime = forms.IntegerField(label="Rate the genres (1-5): Crime: ", min_value=1, max_value=5)
	fantasy = forms.IntegerField(label="Rate the genres (1-5): Fantasy: ", min_value=1, max_value=5)
	fiction = forms.IntegerField(label="Rate the genres (1-5): Fiction: ", min_value=1, max_value=5)
	horror = forms.IntegerField(label="Rate the genres (1-5): Horror: ", min_value=1, max_value=5)
	humor = forms.IntegerField(label="Rate the genres (1-5): Humor: ", min_value=1, max_value=5)
	mystery = forms.IntegerField(label="Rate the genres (1-5): Mystery: ", min_value=1, max_value=5)
	nonfiction = forms.IntegerField(label="Rate the genres (1-5): Non-Fiction: ", min_value=1, max_value=5)
	romance = forms.IntegerField(label="Rate the genres (1-5): Romance: ", min_value=1, max_value=5)
	suspense = forms.IntegerField(label="Rate the genres (1-5): Suspense: ",min_value=1, max_value=5)
	sports = forms.IntegerField(label="Rate the genres (1-5): Sports: ",min_value=1, max_value=5)
	young_adult = forms.IntegerField(label="Rate the genres (1-5): Young Adult: ", min_value=1, max_value=5)
	# genres = forms.CharField(label = question, max_length=50)
	# genres = forms.MultipleChoiceField(label = question, choices = Choices)
	average_read_time = forms.MultipleChoiceField(label = "How often do you read?", choices = R)
	last_book = forms.CharField(label="What is the last book you read? ", max_length=100)
	rating = forms.MultipleChoiceField(label = "How would you rate that book?",choices = Stars )
	favorite_author = forms.CharField(label = "Who is your favorite author", max_length=100)


class UpdateSurveyForm(forms.Form):
	# question = "What are you favorite genres? Options: Art, Biography, Business, Classics, Crime, Fantasy, Fiction, Horror, Humor, Mystery, Non-Fiction, Romance, Suspense, Sports, Young Adult"
	art = forms.IntegerField(label="Rate the genre (1-5): Art: ", min_value=1, max_value=5)
	bio = forms.IntegerField(label="Rate the genre (1-5): Biography: ", min_value=1, max_value=5)
	business = forms.IntegerField(label="Rate the genres (1-5): Business: ", min_value=1, max_value=5)
	classics = forms.IntegerField(label="Rate the genres (1-5): Classics: ", min_value=1, max_value=5)
	crime = forms.IntegerField(label="Rate the genres (1-5): Crime: ", min_value=1, max_value=5)
	fantasy = forms.IntegerField(label="Rate the genres (1-5): Fantasy: ", min_value=1, max_value=5)
	fiction = forms.IntegerField(label="Rate the genres (1-5): Fiction: ", min_value=1, max_value=5)
	horror = forms.IntegerField(label="Rate the genres (1-5): Horror: ", min_value=1, max_value=5)
	humor = forms.IntegerField(label="Rate the genres (1-5): Humor: ", min_value=1, max_value=5)
	mystery = forms.IntegerField(label="Rate the genres (1-5): Mystery: ", min_value=1, max_value=5)
	nonfiction = forms.IntegerField(label="Rate the genres (1-5): Non-Fiction: ", min_value=1, max_value=5)
	romance = forms.IntegerField(label="Rate the genres (1-5): Romance: ", min_value=1, max_value=5)
	suspense = forms.IntegerField(label="Rate the genres (1-5): Suspense: ",min_value=1, max_value=5)
	sports = forms.IntegerField(label="Rate the genres (1-5): Sports: ",min_value=1, max_value=5)
	young_adult = forms.IntegerField(label="Rate the genres (1-5): Young Adult: ", min_value=1, max_value=5)
	# genres = forms.CharField(label = question, max_length=50)
	# genres = forms.MultipleChoiceField(label = question, choices = Choices)


        