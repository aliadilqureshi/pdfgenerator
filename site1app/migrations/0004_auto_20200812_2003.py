# Generated by Django 3.1 on 2020-08-12 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1app', '0003_my_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report_File_Upload_Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generated_report_file_upload', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='my_table',
        ),
    ]
