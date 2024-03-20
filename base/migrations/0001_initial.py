# Generated by Django 4.2.9 on 2024-03-14 03:47

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Email",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email_use_tls",
                    models.BooleanField(blank=True, default=True, null=True),
                ),
                ("email_host", models.CharField(max_length=1024)),
                ("email_host_user", models.CharField(max_length=255)),
                ("email_host_password", models.CharField(max_length=255)),
                (
                    "email_port",
                    models.PositiveSmallIntegerField(
                        blank=True, default=587, null=True
                    ),
                ),
            ],
        ),
    ]
