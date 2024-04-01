# Generated by Django 5.0.2 on 2024-03-29 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_board', '0006_category_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('middle', 'Middle'), ('urgent', 'Urgent')], max_length=10, null=True),
        ),
    ]
