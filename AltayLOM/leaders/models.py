from django.db import models


# Модель пользователя
class User(models.Model):
    class Meta:
        verbose_name = 'Пользователь'

    def __str__(self):
        return "{} ({})".format(str(self.title), str(self.url))

    def __convert__(self):
        pass

    name = models.CharField(verbose_name='Имя', null=True)
    surname = models.CharField(verbose_name='Фамилия', null=True)
    second_Name = models.CharField(verbose_name='Отчество', null=True)
    voices = models.IntegerField(verbose_name='Голоса', null=True)
    place = models.CharField(verbose_name='Город (Район)', null=True)
    email = models.EmailField(verbose_name='Email', null=True)
    phone = models.CharField(verbose_name='Телефон', null=True)
    #photo = models.ImageField(verbose_name='Фото', , upload_to='images', null=True)
    voice_status = models.BooleanField(verbose_name='Мой голос')


#Модель заявки
class Action(models.Model):
    class Meta:
        verbose_name = 'Заявка'

    def __str__(self):
        return "{} ({})".format(str(self.title), str(self.url))

    def __convert__(self):
        pass

    def show_short_content(self):
        return self.content[:40]

    title = models.CharField(verbose_name='Предложение', null=True)
    description = models.CharField(verbose_name='Описание', null=True)
    date_init = models.DateTimeField(verbose_name='Время подачи', null=True)
    status = models.BooleanField(verbose_name='Статус исполнения')
    date_exec = models.DateTimeField(verbose_name='Время Исполнения', null=True)
