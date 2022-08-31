from django.db import models

# Create your models here.


class Partner(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название компании')
    desc = models.TextField(verbose_name='Описание')
    logo = models.ImageField(upload_to='partners/', verbose_name='Логотип', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return self.name


class Advantage(models.Model):
    img = models.ImageField(upload_to='adventages/', verbose_name='Иконка')
    text = models.CharField(max_length=30, verbose_name='Текст')

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'


class Application(models.Model):
    name = models.CharField(max_length=25, verbose_name='Имя')
    phone = models.CharField(max_length=13, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='E-mail')
    comment = models.TextField(verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявка'