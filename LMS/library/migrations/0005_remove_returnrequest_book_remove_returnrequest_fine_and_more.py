# Generated by Django 5.0.3 on 2024-03-16 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_returnrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='returnrequest',
            name='book',
        ),
        migrations.RemoveField(
            model_name='returnrequest',
            name='fine',
        ),
        migrations.RemoveField(
            model_name='returnrequest',
            name='user',
        ),
        migrations.AlterField(
            model_name='fine',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
