# Generated by Django 3.0.5 on 2020-11-20 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0017_allocation_allocating_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocation',
            name='quantity',
        ),
    ]