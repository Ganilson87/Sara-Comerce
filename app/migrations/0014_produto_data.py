# Generated by Django 3.2.4 on 2021-08-02 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_produto_disponibilidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default='2021-08-02 17:31'),
            preserve_default=False,
        ),
    ]
