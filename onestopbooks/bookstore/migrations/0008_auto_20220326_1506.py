# Generated by Django 3.1.3 on 2022-03-26 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0007_auto_20220326_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='rentitem',
            name='quantity1',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
