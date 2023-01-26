# Generated by Django 4.1.5 on 2023-01-24 02:32

import LibraryApp.models
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
            name='Auther',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15)),
                ('Loc', models.CharField(max_length=15)),
                ('About', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15)),
                ('Price', models.PositiveIntegerField()),
                ('Desc', models.CharField(max_length=100)),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='LibraryApp.auther')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FName', models.CharField(max_length=10)),
                ('LName', models.CharField(max_length=10)),
                ('TelNo', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issued_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_date', models.DateField(auto_now=True)),
                ('expiry_date', models.DateField(default=LibraryApp.models.expiry)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='LibraryApp.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issued_books', to='LibraryApp.student')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='LibraryApp.category'),
        ),
    ]
