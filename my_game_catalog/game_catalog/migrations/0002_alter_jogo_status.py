# Generated by Django 5.1.3 on 2024-12-04 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='status',
            field=models.CharField(choices=[('quero_jogar', 'Quero Jogar'), ('jogando', 'Jogando'), ('abandonado', 'Abandonado'), ('zerado', 'Zerado')], default='quero_jogar', max_length=20),
        ),
    ]