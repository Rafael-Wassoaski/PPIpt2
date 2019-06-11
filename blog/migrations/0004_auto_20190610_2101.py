# Generated by Django 2.2.1 on 2019-06-11 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190610_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.CharField(choices=[('AV', 'Aventura'), ('PR', 'Personagem'), ('IT', 'Item'), ('FC', 'Ficha'), ('TM', 'Tema Livre')], default='AV', max_length=2, verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='images/', verbose_name='Capa'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Postagem'),
        ),
    ]
