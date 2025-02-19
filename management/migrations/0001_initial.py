# Generated by Django 5.1 on 2024-09-09 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('blood_type', models.CharField(max_length=3)),
                ('organ', models.CharField(max_length=50)),
                ('contactinfo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('blood_type', models.CharField(max_length=3)),
                ('organ', models.CharField(max_length=15)),
                ('contactinfo', models.CharField(max_length=50)),
            ],
        ),
    ]
