from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
]

urlpatterns += staticfiles_urlpatterns()