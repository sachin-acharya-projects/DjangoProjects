# Generated by Django 3.1.5 on 2021-02-07 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0002_auto_20210207_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='persons',
            name='image',
            field=models.ImageField(default='', upload_to='homeapp/images'),
        ),
    ]
