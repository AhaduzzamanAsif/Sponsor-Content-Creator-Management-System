# Generated by Django 4.1 on 2024-05-28 08:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0012_rename_conversation_chatroom_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
