# Generated by Django 3.2.7 on 2021-10-01 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementapp', '0004_alter_userreg_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='WorkDone',
            field=models.BooleanField(default=False),
        ),
    ]
