# Generated by Django 4.2.9 on 2024-03-14 05:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="email",
            name="email_host",
        ),
        migrations.RemoveField(
            model_name="email",
            name="email_port",
        ),
        migrations.RemoveField(
            model_name="email",
            name="email_use_tls",
        ),
    ]
