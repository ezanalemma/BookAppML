from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('rating/', views.RatingView.as_view(), name='rating'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('upload-csv/', views.books_upload, name='books_upload'),
    path('upload-rating/', views.rating_upload, name='rating_upload'),
    path('survey/', views.survey.as_view(), name='survey')
]
