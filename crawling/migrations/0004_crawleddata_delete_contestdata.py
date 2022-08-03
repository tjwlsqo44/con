# Generated by Django 4.0.6 on 2022-07-19 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0003_contestdata_delete_contest'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrawledData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('due', models.TextField()),
                ('link', models.TextField()),
            ],
            options={
                'db_table': 'crawling_crawleddata',
            },
        ),
        migrations.DeleteModel(
            name='ContestData',
        ),
    ]