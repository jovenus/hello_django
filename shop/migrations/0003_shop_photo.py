# Generated by Django 2.1.5 on 2019-02-20 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190219_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
