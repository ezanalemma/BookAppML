from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Rating, Book, UserSurvey, Survey

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Rating)
admin.site.register(Book)
admin.site.register(UserSurvey)
admin.site.register(Survey)

#
#admin.site.register(MyCSvModel)