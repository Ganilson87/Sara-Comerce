# Generated by Django 3.2.4 on 2021-07-07 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_produto_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='usuario',
        ),
    ]