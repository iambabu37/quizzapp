from django.contrib import admin
from .models import *

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text',)  # Display fields in the admin list view
    search_fields = ('question',)  # Enable search by question text

class OptionAdmin(admin.ModelAdmin):
    list_display = ('text','is_correct')
    search_fields = ('text',)

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    search_fields= ('title',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Option,OptionAdmin)
admin.site.register(Quiz,QuizAdmin)
admin.site.register(QuizAttempt)

# admin.site.register(Subject)
# admin.site.register(TestAnswer)
# admin.site.register(Quiz,QuizAdmin)
# admin.site.register(Option,OptionAdmin)
# admin.site.register(QuizAttempt)