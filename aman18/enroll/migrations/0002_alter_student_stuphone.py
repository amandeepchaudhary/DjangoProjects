# Generated by Django 4.1.1 on 2022-10-16 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='stuphone',
            field=models.BigIntegerField(),
        ),
    ]
