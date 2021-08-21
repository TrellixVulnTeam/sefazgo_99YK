# Generated by Django 2.2.3 on 2019-07-07 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiscalizacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_razao_social', models.CharField(max_length=255)),
                ('inscricao_municipal', models.CharField(blank=True, max_length=32, null=True)),
                ('informacoes_adicionais', models.CharField(blank=True, max_length=1055, null=True)),
                ('cnpj', models.CharField(blank=True, max_length=32, null=True)),
                ('nome_fantasia', models.CharField(blank=True, max_length=255, null=True)),
                ('inscricao_estadual', models.CharField(blank=True, max_length=32, null=True)),
                ('tipo_endereco', models.CharField(blank=True, choices=[('UNI', 'Único'), ('RES', 'Residencial'), ('COM', 'Comercial'), ('COB', 'Cobrança'), ('ENT', 'Entrega'), ('OUT', 'Outro')], max_length=3, null=True)),
                ('logradouro', models.CharField(blank=True, max_length=255, null=True)),
                ('numero', models.CharField(blank=True, max_length=16, null=True)),
                ('bairro', models.CharField(blank=True, max_length=64, null=True)),
                ('complemento', models.CharField(blank=True, max_length=64, null=True)),
                ('pais', models.CharField(blank=True, default='Brasil', max_length=32, null=True)),
                ('municipio', models.CharField(blank=True, max_length=64, null=True)),
                ('cep', models.CharField(blank=True, max_length=16, null=True)),
                ('uf', models.CharField(blank=True, choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('EX', 'EX'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=3, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='fiscal',
            options={'verbose_name': 'Fiscal', 'verbose_name_plural': 'Fiscais'},
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_telefone', models.CharField(blank=True, choices=[('FIX', 'Fixo'), ('CEL', 'Celular'), ('FAX', 'Fax'), ('OUT', 'Outro')], max_length=8, null=True)),
                ('telefone', models.CharField(max_length=32)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='telefone', to='fiscalizacao.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email', to='fiscalizacao.Empresa')),
            ],
        ),
    ]