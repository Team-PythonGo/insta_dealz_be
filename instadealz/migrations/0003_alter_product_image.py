# Generated by Django 4.0.4 on 2022-05-12 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instadealz', '0002_product_description_product_details_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(default='', max_length=256),
        ),
    ]
