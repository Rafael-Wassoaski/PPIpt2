# Generated by Django 2.0.13 on 2019-05-19 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='rosto',
            field=models.ImageField(blank=True, default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='images/'),
        ),
    ]
