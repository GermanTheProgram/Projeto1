# Generated by Django 4.1.3 on 2022-12-02 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_usuario_senha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='senha',
            field=models.EmailField(max_length=25),
        ),
    ]
