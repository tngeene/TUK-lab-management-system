# Generated by Django 3.0.5 on 2020-06-08 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0005_auto_20200608_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocation',
            name='allocation_duration',
        ),
        migrations.AddField(
            model_name='allocation',
            name='is_returned',
            field=models.BooleanField(default=False),
        ),
    ]
