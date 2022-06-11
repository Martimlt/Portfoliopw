# Generated by Django 4.0.4 on 2022-06-11 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0032_projeto_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjetoFinalDeCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('resumo', models.CharField(max_length=200)),
                ('imagem', models.ImageField(upload_to='')),
                ('relatorio', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('video', models.URLField(blank=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.pessoa')),
            ],
        ),
    ]
