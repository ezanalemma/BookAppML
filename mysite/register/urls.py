from django.urls import path

from polls import views as v 

app_name = 'register'
urlpatterns = [
    path('../survey/', v.survey.as_view(), name='survey')
]
