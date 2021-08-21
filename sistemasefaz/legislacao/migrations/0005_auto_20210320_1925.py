# Generated by Django 2.2.3 on 2021-03-20 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legislacao', '0004_auto_20200401_1756'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Secretaria',
            new_name='Orgao',
        ),
        migrations.DeleteModel(
            name='Noticia',
        ),
        migrations.AlterModelOptions(
            name='orgao',
            options={'verbose_name': 'Orgão', 'verbose_name_plural': 'Orgãos'},
        ),
        migrations.RenameField(
            model_name='lei',
            old_name='secretaria',
            new_name='orgao',
        ),
    ]