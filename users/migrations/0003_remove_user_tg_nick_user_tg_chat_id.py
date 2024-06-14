# Generated by Django 5.0.6 on 2024-06-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tg_nick',
        ),
        migrations.AddField(
            model_name='user',
            name='tg_chat_id',
            field=models.CharField(blank=True, default=None, max_length=35, null=True, verbose_name='id чата в телеграм'),
        ),
    ]
