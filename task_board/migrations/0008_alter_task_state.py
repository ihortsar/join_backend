# Generated by Django 5.0.2 on 2024-03-29 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_board', '0007_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
