# Generated by Django 4.2.2 on 2023-07-24 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('safo_eshiklar', '0005_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='No',
            new_name='product_id',
        ),
    ]