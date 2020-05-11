from django.shortcuts import render, get_object_or_404
import csv, io
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import permission_required
from .forms import SurveyForm, UpdateSurveyForm
from home.models import UserBook
from .models import Choice, Question, Rating, Book, Survey, UserSurvey

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
    

# class update(generic.DetailView):
#     template_name = 'surveyUpdate.html'

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
            art = form.cleaned_data['art']
            bio = form.cleaned_data['bio']
            business = form.cleaned_data['business']
            classics = form.cleaned_data['classics']
            crime = form.cleaned_data['crime']
            fantasy = form.cleaned_data['fantasy']
            fiction = form.cleaned_data['fiction']
            horror = form.cleaned_data['horror']
            humor = form.cleaned_data['humor']
            mystery = form.cleaned_data['mystery']
            nonfiction = form.cleaned_data['nonfiction']
            romance = form.cleaned_data['romance']
            suspense = form.cleaned_data['suspense']
            sports = form.cleaned_data['sports']
            young_adult = form.cleaned_data['young_adult']

            read_time = form.cleaned_data['average_read_time']
            book = form.cleaned_data['last_book']
            rate = form.cleaned_data['rating']
            fav_author = form.cleaned_data['favorite_author']
            survey = Survey.objects.create(username= name,
                art=art,
                biography=bio,
                business=business,
                classics=classics,
                crime=crime,
                fantasy=fantasy,
                fiction=fiction,
                horror=horror,
                humor=humor,
                mystery=mystery,
                nonfiction=nonfiction,
                romance=romance,
                suspense=suspense,
                sports=sports,
                young_adult=young_adult,
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


def get_update_survey(request):
    template_name = "polls/surveyUpdate.html"
    user1 = request.user
    if request.method == 'POST':
        form = UpdateSurveyForm(request.POST)
        if form.is_valid():
            art = form.cleaned_data['art']
            bio = form.cleaned_data['bio']
            business = form.cleaned_data['business']
            classics = form.cleaned_data['classics']
            crime = form.cleaned_data['crime']
            fantasy = form.cleaned_data['fantasy']
            fiction = form.cleaned_data['fiction']
            horror = form.cleaned_data['horror']
            humor = form.cleaned_data['humor']
            mystery = form.cleaned_data['mystery']
            nonfiction = form.cleaned_data['nonfiction']
            romance = form.cleaned_data['romance']
            suspense = form.cleaned_data['suspense']
            sports = form.cleaned_data['sports']
            young_adult = form.cleaned_data['young_adult']
            # survey = Survey.objects.filter(username=user1.username)
            survey = None
            for s in Survey.objects.all():
                if s.username == user1.username:
                    survey = s
            if survey:
                survey.art = art
                survey.biography=bio
                survey.business=business
                survey.classics=classics
                survey.crime=crime
                survey.fantasy=fantasy
                survey.fiction=fiction
                survey.horror=horror
                survey.humor=humor
                survey.mystery=mystery
                survey.nonfiction=nonfiction
                survey.romance=romance
                survey.suspense=suspense
                survey.sports=sports
                survey.young_adult=young_adult

            # survey = Survey.objects.create(username= name,
            #     art=art,
            #     biography=bio,
            #     business=business,
            #     classics=classics,
            #     crime=crime,
            #     fantasy=fantasy,
            #     fiction=fiction,
            #     horror=horror,
            #     humor=humor,
            #     mystery=mystery,
            #     nonfiction=nonfiction,
            #     romance=romance,
            #     suspense=suspense,
            #     sports=sports,
            #     young_adult=young_adult,
            #     average_read_time = read_time,
            #     last_book = book,
            #     rating = rate,
            #     favorite_author = fav_author
            # )
            # user_survey = UserSurvey.objects.create(username = user1.username,survey_results = survey)
            survey.save()
            # user_survey.save()
            return HttpResponseRedirect('/home')
    else:
        form = UpdateSurveyForm()

    return render(request, template_name, {'form': form})

