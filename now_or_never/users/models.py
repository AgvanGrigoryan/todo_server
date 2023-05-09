from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)

    def __str__(self):
        return str(self.username)

    def get_absolute_url(self):
        return reverse('user_profile', args=[str(self.username)])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
