# Generated by Django 5.0.6 on 2024-06-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hdver2', '0012_rename_reports_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='employee',
        ),
        migrations.AddField(
            model_name='report',
            name='date_created',
            field=models.DateTimeField(null=True),
        ),
    ]
