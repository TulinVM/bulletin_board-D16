# Generated by Django 3.1.7 on 2021-03-28 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0003_auto_20210321_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='declaration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_declaration', to='bulletin.declaration', verbose_name='обявление'),
        ),
    ]
