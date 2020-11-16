# Generated by Django 3.0.5 on 2020-11-16 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0005_lab_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='school',
        ),
        migrations.AddField(
            model_name='lab',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='labs', to='schools.School'),
        ),
    ]
