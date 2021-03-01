# Generated by Django 3.1.2 on 2021-02-09 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingby', '0009_auto_20210208_1532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='suppler_email',
            new_name='supplier_email',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='suppler_name',
            new_name='supplier_name',
        ),
        migrations.RemoveField(
            model_name='productorder',
            name='units_type',
        ),
        migrations.AlterField(
            model_name='producttype',
            name='prod_type',
            field=models.CharField(choices=[('мешки, кг', 'Мешки - кг'), ('ящики, шт', 'Ящики - шт'), ('ящики, кг', 'Ящики - кг')], max_length=15, verbose_name='Тип тары'),
        ),
        migrations.DeleteModel(
            name='Measure',
        ),
    ]
