from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.detail, name='detail'),
]

urlpatterns += staticfiles_urlpatterns()