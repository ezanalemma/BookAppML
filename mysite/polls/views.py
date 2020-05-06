from django.shortcuts import render, get_object_or_404
import csv, io
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import permission_required


from .models import Choice, Question, Rating, Book


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


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

    

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for choice in question.choice_set.all():
                    if response.POST.get("c" + str(choice_text)) == "clicked":
                        choice.complete = True;
                    else:
                        choice.complete = False;

                    choice.save()
        #selected_choice.votes += 1
        #selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from bein g posted twice if a
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
            art = column[1],
            biography = column[2],
            business = column[3],
            chick_lit = column[4],
            childrens = column[5],
            christian = column[6],
            classics = column[7],
            comics = column[8],
            contemporary = column[9],
            cookbooks = column[10],
            crime =  column[11],
            ebooks =  column[12],
            fantasy =  column[13],
            fiction =  column[14],
            gay_lesbian =  column[15],
            graphic_novels =  column[16],
            historical_fiction =  column[17],
            history =  column[18],
            horror =  column[19],
            humor =  column[20],
            manga =  column[21],
            memoir =  column[22],
            music =  column[23],
            mystery =  column[24],
            nonfiction =  column[25],
            paranormal =  column[26],
            philosophy =  colummn[27],
            poetry = column[28],
            psychology =  column[29],
            religion =  column[30],
            romance =  column[31],
            science =  column[32],
            science_fiction =  column[33],
            self_help =  column[34],
            suspense =  column[35],
            spirituality =  column[36],
            sports =  column[38],
            thriller =  column[39],
            travel =  column[40],
            young_adult =  column[41]
        )
    context ={}
    return render(request, template_name, context)