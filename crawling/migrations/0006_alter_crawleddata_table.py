# Generated by Django 4.0.6 on 2022-07-19 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0005_alter_crawleddata_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='crawleddata',
            table='crawled_data',
        ),
    ]
