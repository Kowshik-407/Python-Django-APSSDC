# Generated by Django 3.1 on 2020-08-11 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty', '0003_auto_20200811_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='Branch',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='Mobile',
        ),
    ]
