# Generated by Django 4.1.1 on 2022-10-08 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('stuid', models.IntegerField(primary_key=True, serialize=False)),
                ('stuname', models.CharField(max_length=100)),
                ('stumail', models.EmailField(max_length=100)),
                ('stupass', models.CharField(max_length=100)),
                ('stuclass', models.IntegerField()),
                ('stuPhone', models.BigIntegerField()),
            ],
        ),
    ]
