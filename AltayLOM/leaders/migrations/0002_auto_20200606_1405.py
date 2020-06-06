# Generated by Django 3.0 on 2020-06-06 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='action',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to='images', verbose_name='Фото'),
        ),
    ]
