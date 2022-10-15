# Generated by Django 4.1.1 on 2022-10-15 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sturoll', models.IntegerField()),
                ('stufname', models.CharField(max_length=70)),
                ('stulname', models.CharField(max_length=70)),
                ('stuemail', models.EmailField(max_length=254)),
                ('stuphone', models.BigIntegerField()),
            ],
        ),
    ]
