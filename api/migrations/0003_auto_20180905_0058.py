# Generated by Django 2.1 on 2018-09-05 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_img',
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='the user', max_length=120),
            preserve_default=False,
        ),
    ]