# Generated by Django 4.0.4 on 2022-06-11 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0034_projetofinaldecurso_left_projetofinaldecurso_right'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetofinaldecurso',
            name='orientador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='portfolio.pessoa'),
        ),
    ]
