# Generated by Django 3.0.3 on 2020-05-09 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20200506_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.BooleanField(),
        ),
    ]