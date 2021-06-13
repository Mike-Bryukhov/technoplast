# Generated by Django 3.1.2 on 2021-06-02 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landingby', '0015_auto_20210602_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='supplier_name',
            field=models.ForeignKey(default='SUPPLIER DEFAULT NAME', on_delete=django.db.models.deletion.PROTECT, to='landingby.supplier', verbose_name='Имя поставщика'),
        ),
    ]