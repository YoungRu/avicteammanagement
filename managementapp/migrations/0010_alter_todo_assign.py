# Generated by Django 3.2.7 on 2021-10-07 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementapp', '0009_alter_todo_assign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Assign',
            field=models.ManyToManyField(null=True, to='managementapp.UserReg'),
        ),
    ]