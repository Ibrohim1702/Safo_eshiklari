# Generated by Django 4.2.2 on 2023-06-13 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=128, unique=True),
            preserve_default=False,
        ),
    ]
