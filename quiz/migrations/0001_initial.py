# Generated by Django 2.0.13 on 2019-05-12 19:13

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
            name='Pergunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('categoria', models.CharField(choices=[('AV', 'Aventura'), ('PR', 'Personagem'), ('IT', 'Item'), ('FC', 'Ficha'), ('TM', 'Tema Livre')], default='AV', max_length=2)),
                ('numPerguntas', models.IntegerField()),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.CharField(max_length=200)),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Pergunta')),
            ],
        ),
        migrations.AddField(
            model_name='pergunta',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz'),
        ),
    ]
