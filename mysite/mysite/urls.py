"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from register import views as v
from polls import views as views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path("login", v.login_request, name="login"),
    path("logout", v.logout_request, name="logout"),
    path('register/', v.register, name="register"),
    path("upload-csv/", views.books_upload, name='books_upload'),
    path("upload-rating/", views.rating_upload, name='rating_upload'),
    path("survey/", views.get_survey, name='survey')
    # path('views/', include('home.urls')),
]

# urlpatterns += [
#     path('', RedirectView.as_view(url='home/', permanent=True)),
# ]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)