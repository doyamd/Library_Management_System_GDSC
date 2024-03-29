# Generated by Django 5.0.3 on 2024-03-14 16:27

import django.db.models.deletion
import library.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Author_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=4)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Genre_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_out_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(default=library.models.expiry)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Publisher_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Publication_year', models.DateField()),
                ('Number_of_copies', models.PositiveIntegerField()),
                ('cover', models.ImageField(upload_to='')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.author')),
                ('genre', models.ManyToManyField(to='library.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
        ),
    ]
