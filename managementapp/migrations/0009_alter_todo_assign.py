# Generated by Django 3.2.7 on 2021-10-02 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementapp', '0008_todo_assign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Assign',
            field=models.ManyToManyField(blank=True, to='managementapp.UserReg'),
        ),
    ]