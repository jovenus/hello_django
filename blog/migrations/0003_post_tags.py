# Generated by Django 2.1.5 on 2019-02-18 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.TextField(default='', max_length=100),
            preserve_default=False,
        ),
    ]