# Generated by Django 3.0.5 on 2020-11-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0013_auto_20201116_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
