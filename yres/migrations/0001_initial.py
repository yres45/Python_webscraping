# Generated by Django 2.1.3 on 2019-03-06 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('track', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('point', models.CharField(max_length=100)),
            ],
        ),
    ]
