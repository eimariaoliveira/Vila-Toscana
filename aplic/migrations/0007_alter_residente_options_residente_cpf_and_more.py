# Generated by Django 4.2.16 on 2024-10-06 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0006_administrador_alter_evento_nome_atividade'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='residente',
            options={'verbose_name': 'Residente', 'verbose_name_plural': 'Residentes'},
        ),
        migrations.AddField(
            model_name='residente',
            name='cpf',
            field=models.CharField(default='000.000.000-00', max_length=100, verbose_name='CPF'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='residente',
            name='email',
            field=models.EmailField(blank=True, max_length=100, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='residente',
            name='nome',
            field=models.CharField(default='Nome Padrão', max_length=100, verbose_name='Nome'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='residente',
            name='senha',
            field=models.CharField(blank=True, max_length=50, verbose_name='Senha'),
        ),
        migrations.AlterField(
            model_name='residente',
            name='data_nascimento',
            field=models.DateField(blank=True, help_text='Formato DD/MM/AAAA', null=True, verbose_name='Data de Nascimento'),
        ),
    ]
