# Generated by Django 3.0.7 on 2022-10-30 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=11, unique=True)),
                ('bank_id', models.CharField(max_length=11)),
                ('branch', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=11)),
                ('city', models.CharField(max_length=11)),
                ('district', models.CharField(max_length=11)),
                ('state', models.CharField(max_length=11)),
                ('bank_name', models.CharField(max_length=11)),
            ],
        ),
    ]
