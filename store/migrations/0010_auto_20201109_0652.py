# Generated by Django 2.1.5 on 2020-11-09 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20201109_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
