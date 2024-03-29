# Generated by Django 3.0.5 on 2020-11-16 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0014_equipment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='is_lost',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='equipment',
            name='price_to_pay',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
