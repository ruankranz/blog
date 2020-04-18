from django.contrib import admin
from krankit.polls.models import Question, Choice, ChoiceVote

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(ChoiceVote)
