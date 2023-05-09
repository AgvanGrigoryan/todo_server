from django.contrib import admin
from django.template.defaultfilters import length
from django.utils.safestring import mark_safe

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
    list_display = ('id', 'hex', 'color_miniature')
    list_display_links = ('id', 'hex')
    fields = ('hex', 'color_miniature')
    readonly_fields = ('color_miniature',)

    def color_miniature(self, obj):
        return mark_safe(f'<div style="width:20px;height:20px;border-radius:50%;background-color:#{obj.hex}"></div>')

    color_miniature.short_description = "Предпросмотр Цвета"

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completionDate', 'author', 'folder', 'isDone')
    list_display_links = ('id', 'title')
    list_filter = ('isDone', 'author', 'folder')
    list_editable = ('isDone',)
