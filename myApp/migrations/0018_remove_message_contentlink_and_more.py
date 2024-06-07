# Generated by Django 4.1 on 2024-05-29 15:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0017_message_contentlink_message_isadapproved_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="contentLink",
        ),
        migrations.RemoveField(
            model_name="message",
            name="isAdApproved",
        ),
        migrations.RemoveField(
            model_name="message",
            name="isPaymentComplete",
        ),
        migrations.RemoveField(
            model_name="message",
            name="isSpApproved",
        ),
        migrations.AddField(
            model_name="chatroom",
            name="contentLink",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="chatroom",
            name="isAdApproved",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="chatroom",
            name="isPaymentComplete",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="chatroom",
            name="isSpApproved",
            field=models.BooleanField(default=False),
        ),
    ]