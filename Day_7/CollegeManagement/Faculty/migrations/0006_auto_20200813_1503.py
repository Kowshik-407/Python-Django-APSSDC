# Generated by Django 3.1 on 2020-08-13 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0005_auto_20200811_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='Branch',
            field=models.CharField(choices=[('ECE', 'ece'), ('CSE', 'cse'), ('EEE', 'eee')], max_length=10),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='Mobile',
            field=models.CharField(max_length=10),
        ),
    ]
