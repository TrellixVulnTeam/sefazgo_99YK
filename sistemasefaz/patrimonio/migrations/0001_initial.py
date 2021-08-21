# Generated by Django 2.2.3 on 2021-01-24 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
            },
        ),
        migrations.CreateModel(
            name='Patrimonio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Baixado', 'Baixado')], max_length=15, verbose_name='Status')),
                ('nota_fiscal', models.IntegerField()),
                ('plaqueta', models.IntegerField()),
                ('numero_matricula', models.IntegerField()),
                ('tipo', models.CharField(choices=[('Mobiliario', 'Mobiliario'), ('Informatica', 'Informatica'), ('outros', 'Outros')], max_length=15, verbose_name='Tipo do Bem')),
                ('data_aquisicao', models.DateTimeField(auto_now=True, verbose_name='Data de Aquisição')),
                ('data_baixa', models.DateTimeField(auto_now=True, verbose_name='Data de Aquisição')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='setor', to='patrimonio.Setor')),
            ],
            options={
                'verbose_name': 'Patrimonio',
                'verbose_name_plural': 'Patrimonios',
            },
        ),
    ]