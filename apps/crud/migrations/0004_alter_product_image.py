# Generated by Django 4.0.2 on 2022-02-25 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='portfolio/images/'),
        ),
    ]