# Generated by Django 3.0.5 on 2020-11-16 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0006_auto_20201116_1246'),
        ('users', '0005_auto_20201116_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='lab',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='schools.Lab'),
        ),
    ]
