# Generated by Django 3.1 on 2020-08-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200814_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='Publication_Date',
            field=models.CharField(max_length=30),
        ),
    ]
