# Generated by Django 3.1.2 on 2020-10-05 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20201005_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
