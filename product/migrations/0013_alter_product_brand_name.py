# Generated by Django 5.0.1 on 2024-01-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_product_brand_name_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand_name',
            field=models.CharField(max_length=100),
        ),
    ]