# Generated by Django 3.0.5 on 2020-04-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axfapp', '0007_auto_20200430_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='childcidname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='goods',
            name='onefree',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='goods',
            name='productname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='goods',
            name='specifics',
            field=models.CharField(max_length=200),
        ),
    ]
