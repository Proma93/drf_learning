# Generated by Django 5.2.4 on 2025-07-21 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_remove_todo_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="timingtodo",
            name="due_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
