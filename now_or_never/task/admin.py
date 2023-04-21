from django.contrib import admin

from task.models import Folder, Task


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'slug')
    list_display_links = ('id', 'name', 'slug')
    list_filter = ('user',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completionDate', 'author', 'folder', 'isDone')
    list_display_links = ('id', 'title')
    list_filter = ('author', 'folder', 'isDone')
    list_editable = ('isDone',)
