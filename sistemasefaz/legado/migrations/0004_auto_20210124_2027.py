# Generated by Django 2.2.3 on 2021-01-24 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legado', '0003_auto_20200406_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagamentos',
            options={'managed': False, 'verbose_name': 'Pagamento', 'verbose_name_plural': 'Pagamentos'},
        ),
        migrations.AlterModelOptions(
            name='titulos',
            options={'managed': False, 'verbose_name': 'Titulo', 'verbose_name_plural': 'Titulos'},
        ),
    ]
