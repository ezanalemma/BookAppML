# Generated by Django 3.0.3 on 2020-05-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooksRead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=0, max_length=30)),
                ('book_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserBook',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('book_id', models.IntegerField(default=0)),
            ],
        ),
    ]
