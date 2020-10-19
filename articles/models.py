from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    # slug = models.SlugField(max_length=150)
    text = models.TextField(verbose_name='Текст')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta():
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
