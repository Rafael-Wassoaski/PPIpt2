# Generated by Django 2.2.1 on 2019-05-27 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='title',
            new_name='titulo',
        ),
    ]