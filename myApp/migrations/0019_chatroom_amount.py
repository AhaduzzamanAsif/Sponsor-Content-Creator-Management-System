# Generated by Django 4.1 on 2024-05-29 15:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0018_remove_message_contentlink_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="chatroom",
            name="amount",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
