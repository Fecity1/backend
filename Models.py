from django.db import models

class Human(models.Model):
    class Meta:
        verbose_name = 'Пользователь'

    def __str__(self):
        return "{} ({})".format(str(self.title), str(self.url))

    def __convert__(self):
        pass

    def show_short_content(self):
        return self.content[:40]

    show_short_content.short_description = "Контент"

    Name = models.CharField(verbose_name='Имя', null=True)
    Surname = models.CharField(verbose_name='Фамилия', null=True)
    Second_Name = models.CharField(verbose_name='Отчество', null=True)
    Voises = models.IntegerField(verbose_name='Голоса, %', null=True)
    Place = models.CharField(verbose_name='Город (Район)', null=True)
    Email = models.EmailField(verbose_name='Email', null=True)
    Phone = models.SmallIntegerField(verbose_name='Телефон, %', null=True)
    #Photo = models.ImageField(verbose_name='Фото', , upload_to='images', null=True)
    VoiseStatus = models.BooleanField(verbose_name='Мой голос')

class Request(models.Model):
    class Meta:
        verbose_name = 'Заявка'

    def __str__(self):
        return "{} ({})".format(str(self.title), str(self.url))

    def __convert__(self):
        pass

    def show_short_content(self):
        return self.content[:40]

    show_short_content.short_description = "Контент"

    Title = models.CharField(verbose_name='Предложение', null=True)
    Request = models.CharField(verbose_name='Описание', null=True)
    DataStart = models.DateTimeField(verbose_name='Время подачи', null=True)
    Status = models.BooleanField(verbose_name='Статус исполнения')
    DataFinal = models.DateTimeField(verbose_name='Время Исполнения', null=True)


class NewsContent(models.Model):
    class Meta:
        verbose_name = 'Контент новостей'
        verbose_name_plural = 'Контенты новостей'

    def __str__(self):
        return "{} ({})".format(str(self.title), str(self.url))

    def __convert__(self):
        pass

    def show_short_content(self):
        return self.content[:40]
    show_short_content.short_description = "Контент"

    news_source = models.ForeignKey(NewsSource, verbose_name='Источник', on_delete=models.SET_NULL, null=True)
    url = models.CharField(verbose_name="Ссылка", max_length=200)
    title = models.CharField(verbose_name="Заголовок", max_length=200, null=True)
    raw_content = models.TextField(verbose_name="Html-код", null=True)
    content = models.TextField(verbose_name="Содержимое", null=True)
    pub_date = models.CharField(verbose_name="Дата публикации", max_length=40, null=True)
    parsing_date = models.DateTimeField(verbose_name="Дата парсинга", auto_now_add=True)