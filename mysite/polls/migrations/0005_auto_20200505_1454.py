# Generated by Django 3.0.3 on 2020-05-05 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200422_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='choice_text',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='question',
        ),
        migrations.AddField(
            model_name='choice',
            name='complete',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn13',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.FloatField(default=0),
        ),
    ]
