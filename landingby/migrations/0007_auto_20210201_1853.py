# Generated by Django 3.1.2 on 2021-02-01 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingby', '0006_auto_20210201_1748'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supplier',
            options={'ordering': ['id'], 'verbose_name': 'Поставщик', 'verbose_name_plural': 'Поставщики'},
        ),
    ]
