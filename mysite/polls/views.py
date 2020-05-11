from django.shortcuts import render, get_object_or_404
import csv, io
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import permission_required
from .forms import SurveyForm
from home.models import UserBook
from .models import Choice, Question, Rating, Book, Survey, UserSurvey


Choices=[
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
]


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    #add individyal form
    template_name = 'polls/results.html'

class RatingView(generic.DetailView):
    #if request.method == 'POST':
    # take care of instance
    #form = RateForm(request.POST, instance=your-listing-instance)
    #if form.is_valid():
       # rate = form.save(commit=False)
        # adding the user here.
#        #rate.save()
    model = Rating
    template_name = 'polls/rating.html'

class survey(generic.DetailView):
    template_name = 'survey.html'
    

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        display_type1 = request.POST.getlist('display', None)
        if not display_type1:
            return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
        for dis in display_type1:
            selected_choice = question.choice_set.get(pk=dis)
            selected_choice.votes = False
            selected_choice.save()
            if selected_choice in question.choice_set.all():
                selected_choice.votes = True
                selected_choice.complete = True
                selected_choice.save()


        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

@permission_required('admin.can_add_log_entry')
def books_upload(request):
    template_name = "polls/books_upload.html"
    prompt={
        'order': 'Order of the CSV should be book_id, good_reads_id, title, authors, year, genre, tag_id, image_url,small_image_url, isbn, isbn13'
        }
    if request.method == 'GET':
        return render(request, template_name, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        message.error(request,'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=','):
        _, created = Book.objects.update_or_create(
            book_id = column[0],
            good_reads_id = column[1],
            title = column[2],
            authors = column[3],
            year = column[4],
            genre = column[5],
            tag_id = column[6],
            image_url = column[7],
            small_image_url = column[8],
            isbn = column[9],
            isbn13 = column[10]
        )
    context ={}
    return render(request, template_name, context)

@permission_required('admin.can_add_log_entry')
def rating_upload(request):
    template_name = "polls/rating_upload.html"
    prompt={
        'order' : 'Upload ratings.csv'
        }
    if request.method == 'GET':
        return render(request, template_name, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        message.error(request,'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=','):
        _, created = Rating.objects.update_or_create(
            user_id = column[0],
            book_id = column[1],
            rating = column[2],
        )
    context ={};
    return render(request, template_name, context);

def get_survey(request):
    template_name = "polls/survey.html"
    user1 = request.user
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['user']
            genres1 = form.cleaned_data['genres']

            for choice in Choices:
                if choice[0] == genres1:
                    genres1 = choice[1]

            read_time = form.cleaned_data['average_read_time']
            book = form.cleaned_data['last_book']
            rate = form.cleaned_data['rating']
            fav_author = form.cleaned_data['favorite_author']
            survey = Survey.objects.create(username= name,
                genres=genres1,
                average_read_time = read_time,
                last_book = book,
                rating = rate,
                favorite_author = fav_author
            )
            user_survey = UserSurvey.objects.create(username = user1.username,survey_results = survey)
            survey.save()
            user_survey.save()
            return HttpResponseRedirect('/home')
    else:
        form = SurveyForm()

    return render(request, template_name, {'form': form})
