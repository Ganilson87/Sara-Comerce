# Generated by Django 3.2.4 on 2021-07-04 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210704_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='prec_prod',
            field=models.IntegerField(verbose_name='Preço'),
        ),
    ]