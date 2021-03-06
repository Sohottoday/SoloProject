# Generated by Django 2.1.15 on 2020-06-18 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upso_num', models.CharField(max_length=30)),
                ('upso_name', models.CharField(max_length=40)),
                ('dong_name', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('area', models.FloatField()),
                ('tell_num', models.TextField(max_length=20)),
                ('upjong', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=30)),
                ('item', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('check_date', models.CharField(max_length=20)),
                ('gu_name', models.CharField(max_length=10)),
            ],
        ),
    ]
