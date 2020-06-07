from django.db import models


# Модель пользователя
class Profile(models.Model):
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    name = models.CharField(verbose_name='Имя', max_length=200, null=True)
    surname = models.CharField(verbose_name='Фамилия', max_length=200, null=True)
    second_Name = models.CharField(verbose_name='Отчество', max_length=200)
    place = models.CharField(verbose_name='Город (Район)', max_length=200)
    email = models.EmailField(verbose_name='Email', null=True)
    phone = models.CharField(verbose_name='Телефон', max_length=200)
    photo = models.ImageField(verbose_name='Фото', upload_to='images')
    leader_status = models.BooleanField(verbose_name='Лидер общественного мнения')
    biography = models.TextField(verbose_name='О себе')
    social_network = models.URLField(verbose_name='Социальные сети')


# Модель заявки
class Action(models.Model):

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    title = models.CharField(verbose_name='Предложение', max_length=200, null=True)
    description = models.CharField(verbose_name='Описание', max_length=200, null=True)
    date_init = models.DateTimeField(verbose_name='Время подачи', null=True)
    status = models.BooleanField(verbose_name='Статус исполнения')
    date_exec = models.DateTimeField(verbose_name='Время Исполнения', null=True)


# Модель Рецензии
class Review(models.Model):
    class Meta:
        verbose_name = 'Рецензия'
        verbose_name_plural = 'Рецензии'

    title = models.CharField(verbose_name='Рецензия', max_length=200, null=True)
    description = models.CharField(verbose_name='Содержание', max_length=200, null=True)
    date_init = models.DateTimeField(verbose_name='Время подачи', null=True)


# Модель Голоса
class Voises(models.Model):
    class Meta:
        verbose_name = 'Голос'
        verbose_name_plural = 'Голоса'

    voices = models.IntegerField(verbose_name='Голоса', null=True)
    voice_status = models.BooleanField(verbose_name='Мой голос')
    voices_negative = models.IntegerField(verbose_name='Отозванные голоса')
    voting_positive = models.IntegerField(verbose_name='Голосований в пользу лидера')