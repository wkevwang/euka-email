# Generated by Django 5.0.3 on 2024-03-15 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_email_email_working'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='daily_sending_limit',
            field=models.SmallIntegerField(default=20),
        ),
    ]
