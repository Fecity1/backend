from django.db import models

# Создать тут модели


# Пример полей
"""
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
"""
