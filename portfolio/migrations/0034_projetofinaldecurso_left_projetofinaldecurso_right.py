# Generated by Django 4.0.4 on 2022-06-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0033_projetofinaldecurso'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetofinaldecurso',
            name='left',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projetofinaldecurso',
            name='right',
            field=models.BooleanField(default=False),
        ),
    ]
