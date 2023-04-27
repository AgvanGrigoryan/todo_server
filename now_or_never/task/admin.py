from django.contrib import admin
from django.template.defaultfilters import length

from task.models import Folder, Task, Color


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'slug', 'post_count')
    list_display_links = ('id', 'name', 'slug')
    list_filter = ('user',)
    fields = ('name', 'user')

    def post_count(self, obj):
        return length(obj.folderTasks.all())
    post_count.short_description = 'Кол. задач в папке'

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'hex')
    list_display_links = ('id', 'hex')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completionDate', 'author', 'folder', 'isDone')
    list_display_links = ('id', 'title')
    list_filter = ('author', 'folder', 'isDone')
    list_editable = ('isDone',)
