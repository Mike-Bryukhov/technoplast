# Generated by Django 3.1.2 on 2021-05-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingby', '0012_auto_20210214_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='supplier_mobile',
            field=models.CharField(max_length=12, verbose_name='Телефон поставщика: +380'),
        ),
    ]
