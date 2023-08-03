# Generated by Django 4.2.4 on 2023-08-03 10:42

from django.db import migrations, models
import django.db.models.deletion
import pereval.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('height', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_1', models.ImageField(max_length=255, upload_to=pereval.utils.get_image_path)),
                ('title_1', models.CharField(max_length=255)),
                ('data_2', models.ImageField(max_length=255, upload_to=pereval.utils.get_image_path)),
                ('title_2', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fam', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('otc', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=18)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(blank=True, max_length=255)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('other_titles', models.CharField(blank=True, max_length=255)),
                ('connect', models.CharField(blank=True, max_length=255)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'Новый'), ('pending', 'Модератор взял в работу'), ('accepted', 'Модерация прошла успешно'), ('rejected', 'Модерация прошла, информация не принята')], default='new', max_length=10)),
                ('level', models.CharField(choices=[('winter-1A', 'Зима-1А'), ('winter-2A', 'Зима-2А'), ('winter-3A', 'Зима-3А'), ('winter-1B', 'Зима-1Б'), ('winter-2B', 'Зима-2Б'), ('winter-3B', 'Зима-3Б'), ('spring-1A', 'Весна-1А'), ('spring-2A', 'Весна-2А'), ('spring-3A', 'Весна-3А'), ('spring-1B', 'Весна-1Б'), ('spring-2B', 'Весна-2Б'), ('spring-3B', 'Весна-3Б'), ('summer-1A', 'Лето-1А'), ('summer-2A', 'Лето-2А'), ('summer-3A', 'Лето-3А'), ('summer-1B', 'Лето-1Б'), ('summer-2B', 'Лето-2Б'), ('summer-3B', 'Лето-3Б'), ('autumn-1A', 'Осень-1А'), ('autumn-2A', 'Осень-2А'), ('autumn-3A', 'Осень-3А'), ('autumn-1B', 'Осень-1Б'), ('autumn-2B', 'Осень-2Б'), ('autumn-3B', 'Осень-3Б')], max_length=10)),
                ('coords', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.coords')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.users')),
            ],
        ),
    ]
