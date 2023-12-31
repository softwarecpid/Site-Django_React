# Generated by Django 4.2.7 on 2023-11-08 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamSoft',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default=1, max_length=100, verbose_name='Name')),
                ('SurName', models.CharField(default=1, max_length=100, verbose_name='SurName')),
                ('Position', models.CharField(default=1, max_length=100, verbose_name='Position')),
                ('Email', models.EmailField(max_length=200, verbose_name='Email')),
                ('Telephone', models.CharField(max_length=15, verbose_name='Telephone')),
                ('CPF', models.CharField(max_length=15, verbose_name='CPF')),
                ('RG', models.CharField(max_length=10, verbose_name='Identity')),
                ('BirthDate', models.CharField(max_length=10, verbose_name='BirthDate')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
