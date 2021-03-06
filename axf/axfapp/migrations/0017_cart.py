# Generated by Django 3.0.5 on 2020-05-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axfapp', '0016_auto_20200506_0059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userAccount', models.CharField(max_length=20)),
                ('productid', models.CharField(max_length=20)),
                ('productnum', models.IntegerField()),
                ('productprice', models.CharField(max_length=20)),
                ('isChose', models.BooleanField(default=True)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=200)),
                ('orderid', models.CharField(default='0', max_length=20)),
                ('idDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
