# Generated by Django 3.0.5 on 2020-11-09 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equipment', '0008_batch_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocation',
            name='student',
        ),
        migrations.AddField(
            model_name='allocation',
            name='allocated_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipment_allocated', to=settings.AUTH_USER_MODEL),
        ),
    ]
