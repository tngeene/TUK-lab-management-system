# Generated by Django 3.0.5 on 2020-05-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200419_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
    ]
