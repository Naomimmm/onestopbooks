# Generated by Django 3.1.3 on 2022-03-02 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=20, max_length=10, verbose_name='price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=100, max_length=10, verbose_name='Quantity'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='thumbnail_pic',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/books', verbose_name='thumbnail_pic'),
        ),
    ]