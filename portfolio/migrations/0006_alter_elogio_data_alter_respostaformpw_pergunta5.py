# Generated by Django 4.0.4 on 2022-05-23 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_elogio_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elogio',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='respostaformpw',
            name='pergunta5',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
