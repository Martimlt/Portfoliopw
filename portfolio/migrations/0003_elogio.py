# Generated by Django 4.0.4 on 2022-05-22 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_pessoa_linkedin_alter_pessoa_outrolink_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elogio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiroNome', models.CharField(max_length=100)),
                ('ultimoNome', models.CharField(max_length=100)),
                ('trabalho', models.CharField(max_length=200)),
                ('elogio', models.CharField(max_length=800)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
