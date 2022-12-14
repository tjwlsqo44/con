# Generated by Django 4.0.6 on 2022-07-25 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0010_remove_swdata_sw_contest_swdata_sw_contest'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpartanEdu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('link', models.TextField()),
            ],
        ),
        migrations.AddConstraint(
            model_name='spartanedu',
            constraint=models.UniqueConstraint(fields=('title', 'link'), name='spartan_notice'),
        ),
    ]
