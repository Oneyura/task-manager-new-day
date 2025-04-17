# Generated by Django 5.2 on 2025-04-17 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0002_task_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='worker', to='task_manager.position'),
        ),
    ]
