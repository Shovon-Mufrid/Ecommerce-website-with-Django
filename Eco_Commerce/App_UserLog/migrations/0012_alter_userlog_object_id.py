# Generated by Django 4.1.5 on 2023-02-27 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_UserLog', '0011_alter_userlog_object_id_alter_userlog_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='object_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
