from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Folder(models.Model):
    name = models.CharField(max_length=15, verbose_name='Название Папки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.user}-{self.name}'

    class Meta:
        verbose_name = 'Папка'
        verbose_name_plural = 'Папки'


class Color(models.Model):
    hex = models.CharField(max_length=6, verbose_name='Цвет',
                           help_text="Указывать в формате HEX(без '#')")

    def __str__(self):
        return self.hex

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class Task(models.Model):
    author = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Описание')
    publicationDate = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    completionDate = models.DateTimeField(verbose_name='Дата выполнения')
    folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Папка')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Цвет Задачи')
    isDone = models.BooleanField(default=False, verbose_name='Выполнен')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

        db_table_comment = "User's tasks"
