# Generated by Django 3.2.9 on 2022-02-26 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]