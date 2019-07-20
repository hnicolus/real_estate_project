# Generated by Django 2.2.3 on 2019-07-15 16:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('garage', models.IntegerField(default=0)),
                ('sqft', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=5)),
                ('image_main', models.ImageField(upload_to='images/%Y/%m/%d/')),
                ('image_1', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
                ('image_2', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
                ('image_3', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
                ('image_4', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
                ('image_5', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
                ('image_6', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor')),
            ],
        ),
    ]