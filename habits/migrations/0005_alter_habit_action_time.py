# Generated by Django 5.0.6 on 2024-06-13 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_alter_habit_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='action_time',
            field=models.DurationField(blank=True, default=None, null=True, verbose_name='время выполнения'),
        ),
    ]