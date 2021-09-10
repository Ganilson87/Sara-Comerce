# Generated by Django 3.2.4 on 2021-08-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_produto_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tipo_prod',
            field=models.CharField(choices=[('Produtos Alimentares', 'Produtos Alimentares'), ('Bebidas', 'Bebidas'), ('Produtos de Limpeza', 'Produtos de Limpeza'), ('Cosméticos', 'Cosméticos')], max_length=100, verbose_name='Tipo de Produto'),
        ),
    ]