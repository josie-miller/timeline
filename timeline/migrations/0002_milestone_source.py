# Generated by Django 5.0.1 on 2024-11-19 19:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("timeline", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="milestone",
            name="source",
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
