# Generated by Django 5.0.3 on 2024-03-15 03:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_email_daily_sending_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='today_email_sent',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='ScheduledEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_email', models.CharField(max_length=255)),
                ('subject', models.TextField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('time_to_send', models.DateTimeField()),
                ('from_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.email')),
            ],
        ),
    ]
