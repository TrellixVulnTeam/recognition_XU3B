# Generated by Django 2.2.5 on 2019-09-23 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aadhar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=9300)),
                ('address_aadhar_no', models.CharField(max_length=9300)),
            ],
        ),
    ]
