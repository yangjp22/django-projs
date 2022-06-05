from django.contrib import admin
from .models import Question, Choice

# Register your models here.
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pubDate", "questionText"]
    fieldsets = [
        (None, {"fields": ["questionText"]}),
        ("Date Information", {"fields": ["pubDate"], "classes": ["collapse"]})
    ]
    inlines = [ChoiceInline]
    
    list_display = ("questionText", "pubDate", "was_published_recently")
    list_filter = ["pubDate"]
    search_fields = ["quesstionText"]
    # list_per_page = 3


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)