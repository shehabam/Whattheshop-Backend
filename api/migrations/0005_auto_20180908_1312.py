# Generated by Django 2.1 on 2018-09-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180908_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_of_purchase',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
