# Generated by Django 4.1.3 on 2023-08-04 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0014_auto_20210424_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='declaration',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
