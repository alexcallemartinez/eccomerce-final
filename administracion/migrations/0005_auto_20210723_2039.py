# Generated by Django 3.1.7 on 2021-07-23 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0004_auto_20210723_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productomodel',
            name='productoFoto',
            field=models.ImageField(db_column='producto_foto', default=0, null=True, upload_to='producto/', verbose_name='Foto del producto'),
        ),
    ]
