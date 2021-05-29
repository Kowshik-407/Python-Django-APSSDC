# Generated by Django 3.1 on 2020-08-13 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, unique=True)),
                ('Age', models.IntegerField(null=True)),
                ('Branch', models.CharField(choices=[('ECE', 'ece'), ('CSE', 'cse'), ('IT', 'it'), ('EEE', 'eee')], max_length=10)),
                ('Mobile', models.CharField(max_length=10)),
                ('Email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]