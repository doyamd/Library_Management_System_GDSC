# Generated by Django 5.0.3 on 2024-03-17 08:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_alter_returnrequest_loan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fine',
            name='status',
        ),
        migrations.AddField(
            model_name='returnrequest',
            name='fine',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.fine'),
        ),
    ]
