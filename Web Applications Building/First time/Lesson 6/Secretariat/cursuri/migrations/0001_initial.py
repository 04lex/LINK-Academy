# Generated by Django 4.2 on 2023-05-30 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=40)),
                ('descriere', models.TextField()),
                ('dificultate', models.IntegerField()),
                ('pret', models.IntegerField()),
                ('public', models.BooleanField()),
            ],
        ),
    ]