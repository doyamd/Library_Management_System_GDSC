# Generated by Django 5.0.3 on 2024-03-17 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_alter_book_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-likes']},
        ),
    ]
