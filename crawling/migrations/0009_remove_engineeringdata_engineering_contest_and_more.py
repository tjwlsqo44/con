# Generated by Django 4.0.6 on 2022-07-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0008_engineeringdata_ideadata_swdata_webdata_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='engineeringdata',
            name='engineering_contest',
        ),
        migrations.RemoveConstraint(
            model_name='ideadata',
            name='idea_contest',
        ),
        migrations.RemoveConstraint(
            model_name='swdata',
            name='Sw_contest',
        ),
        migrations.RemoveConstraint(
            model_name='webdata',
            name='web_contest',
        ),
        migrations.AddConstraint(
            model_name='engineeringdata',
            constraint=models.UniqueConstraint(fields=('title', 'due', 'link'), name='engineering_contest'),
        ),
        migrations.AddConstraint(
            model_name='ideadata',
            constraint=models.UniqueConstraint(fields=('title', 'due', 'link'), name='idea_contest'),
        ),
        migrations.AddConstraint(
            model_name='swdata',
            constraint=models.UniqueConstraint(fields=('title', 'due', 'link'), name='Sw_contest'),
        ),
        migrations.AddConstraint(
            model_name='webdata',
            constraint=models.UniqueConstraint(fields=('title', 'due', 'link'), name='web_contest'),
        ),
    ]