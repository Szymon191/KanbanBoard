from django.contrib import admin

from KanbanBoardApp.models import Task


# Register your models here.


@admin.register(Task)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'status')
