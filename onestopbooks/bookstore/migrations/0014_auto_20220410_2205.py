# Generated by Django 3.1.3 on 2022-04-11 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0013_reviewrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='review',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='reviewrating',
            name='subject',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
