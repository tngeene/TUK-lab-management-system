# Generated by Django 3.0.5 on 2020-10-15 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0006_auto_20200830_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=254)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
