# Generated by Django 3.0.7 on 2020-07-13 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.AddField(
            model_name='contact',
            name='number',
            field=models.CharField(default='', max_length=15),
        ),
    ]
