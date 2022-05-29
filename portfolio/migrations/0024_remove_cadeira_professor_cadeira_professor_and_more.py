# Generated by Django 4.0.4 on 2022-05-29 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0023_projeto_left_projeto_right'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadeira',
            name='professor',
        ),
        migrations.AddField(
            model_name='cadeira',
            name='professor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='portfolio.pessoa'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='cadeira',
            name='professorAuxiliar',
        ),
        migrations.AddField(
            model_name='cadeira',
            name='professorAuxiliar',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='portfolio.pessoa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projeto',
            name='cadeira',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.cadeira'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='competencia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='portfolio.competencia'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='participante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='portfolio.pessoa'),
        ),
    ]