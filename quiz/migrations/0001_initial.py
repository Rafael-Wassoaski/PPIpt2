# Generated by Django 2.2.1 on 2019-06-18 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('categoria', models.CharField(choices=[('AV', 'Aventura'), ('PR', 'Personagem'), ('IT', 'Item'), ('FC', 'Ficha'), ('TM', 'Tema Livre')], default='AV', max_length=2)),
                ('numPerguntas', models.IntegerField()),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.TextField()),
                ('resposta', models.CharField(max_length=200)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz')),
            ],
        ),
    ]
