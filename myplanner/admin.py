from django.contrib import admin
from .models import Task, Quote


class TaskAdmin(admin.ModelAdmin):
    fields = ['user', 'task_name', 'completed']
    list_display = ['user', 'task_name', 'completed', 'date']


class QuoteAdmin(admin.ModelAdmin):
    fields = ['quote_text', 'author']
    list_display = ['quote_text', 'author']


admin.site.register(Task, TaskAdmin)
admin.site.register(Quote, QuoteAdmin)

