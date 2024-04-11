# Generated by Django 5.0.3 on 2024-03-24 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField(max_length=10)),
                ('email', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=300)),
                ('exp', models.IntegerField(max_length=40)),
                ('department', models.CharField(max_length=12)),
                ('working', models.BooleanField(default=True)),
            ],
        ),
    ]