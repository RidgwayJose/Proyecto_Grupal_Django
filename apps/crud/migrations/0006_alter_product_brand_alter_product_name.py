# Generated by Django 4.0.2 on 2022-03-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_remove_product_cod_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=30, verbose_name='marca'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Producto'),
        ),
    ]