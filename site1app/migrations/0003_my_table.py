# Generated by Django 3.1 on 2020-08-11 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1app', '0002_saf_defect_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='my_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_table_number', models.FloatField()),
                ('your_table_number', models.FloatField()),
            ],
        ),
    ]
