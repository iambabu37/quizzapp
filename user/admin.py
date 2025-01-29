from django.contrib import admin
from .models import *

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text','choices','correct_answer', 'question_at')  # Display fields in the admin list view
    search_fields = ('question_text',)  # Enable search by question text

admin.site.register(Question, QuestionAdmin)
admin.site.register(Score)