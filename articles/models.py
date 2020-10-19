from django.contrib.auth.models import User
from django.db import models


class Articles(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Автор')
    title = models.CharField(max_length=150, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta():
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
