# Generated by Django 3.1.7 on 2021-04-18 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0011_auto_20210417_2350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='reviiew',
            new_name='review',
        ),
        migrations.RemoveField(
            model_name='declaration',
            name='review',
        ),
        migrations.AddField(
            model_name='reviews',
            name='declaration',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review_declaration', to='bulletin.declaration', verbose_name='обявление'),
        ),
    ]
