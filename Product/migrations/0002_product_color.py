# Generated by Django 4.1.7 on 2023-03-05 16:32

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=colorful.fields.RGBColorField(default='#fff'),
        ),
    ]
