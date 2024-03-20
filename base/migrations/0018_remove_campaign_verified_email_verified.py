# Generated by Django 5.0.3 on 2024-03-16 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_campaign_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='verified',
        ),
        migrations.AddField(
            model_name='email',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
