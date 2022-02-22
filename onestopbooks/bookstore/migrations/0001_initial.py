# Generated by Django 3.1.2 on 2022-02-21 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=30, verbose_name='isbn')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('authors', models.CharField(max_length=100, verbose_name='authors')),
                ('year_public', models.IntegerField(null=True, verbose_name='year_public')),
                ('publisher', models.CharField(max_length=100, null=True, verbose_name='publisher')),
                ('thumbnail_pic', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='thumbnail_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('address_1', models.CharField(max_length=128, verbose_name='address')),
                ('address_2', models.CharField(blank=True, max_length=128, verbose_name='address continued')),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('zip_code', models.CharField(max_length=5)),
            ],
        ),
    ]
