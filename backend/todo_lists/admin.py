from django.contrib import admin
from .models import Todo_lists

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')



admin.site.register(Todo_lists, TodoAdmin)
