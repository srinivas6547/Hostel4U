# Generated by Django 5.0.4 on 2024-08-14 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OwnerApp', '0009_alter_roomdatabase_bedno'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostellerDataBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostelid', models.IntegerField()),
                ('bedid', models.CharField(max_length=30)),
                ('roomno', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=12, unique=True)),
                ('aadhar', models.CharField(max_length=14, unique=True)),
                ('occupation', models.CharField(max_length=20)),
                ('joindate', models.DateField()),
            ],
        ),
    ]
