# Generated by Django 3.0.8 on 2020-07-11 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200711_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=True, max_length=15),
        ),
    ]
