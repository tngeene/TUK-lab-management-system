# Generated by Django 3.0.5 on 2020-08-30 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import equipment.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schools', '0001_initial'),
        ('equipment', '0003_auto_20200701_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocation',
            name='allocated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='equipment_allocations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='allocation',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allocations', to='schools.Course'),
        ),
        migrations.AlterField(
            model_name='allocation',
            name='equipment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allocations', to='equipment.Equipment'),
        ),
        migrations.AlterField(
            model_name='allocation',
            name='quantity',
            field=models.IntegerField(default=0, validators=[equipment.validators.validate_quantities]),
        ),
        migrations.AlterField(
            model_name='allocation',
            name='student',
            field=models.ForeignKey(blank=True, limit_choices_to={'user_type': 'Student'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipment_allocated', to=settings.AUTH_USER_MODEL),
        ),
    ]
