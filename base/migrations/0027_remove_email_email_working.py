# Generated by Django 5.0.3 on 2024-03-20 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_rename_connected_user_email_email_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='email_working',
        ),
    ]
