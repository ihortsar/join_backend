# Generated by Django 5.0.2 on 2024-04-03 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_board', '0011_user_tasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_users',
            field=models.ManyToManyField(to='task_board.user'),
        ),
    ]
