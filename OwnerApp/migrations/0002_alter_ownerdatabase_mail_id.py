# Generated by Django 5.0.4 on 2024-07-24 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OwnerApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerdatabase',
            name='mail_id',
            field=models.CharField(max_length=50),
        ),
    ]
