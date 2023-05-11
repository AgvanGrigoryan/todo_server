from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    image = models.ImageField(default='users_images/default_user.jpg', upload_to='users_images', blank=True, null=True)

    def __str__(self):
        return str(self.username)

    def get_absolute_url(self):
        return reverse('user_profile')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
