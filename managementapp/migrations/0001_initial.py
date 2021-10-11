# Generated by Django 3.2.7 on 2021-09-30 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Assign_Time', models.DateTimeField(auto_now_add=True, null=True)),
                ('Work', models.CharField(max_length=200)),
                ('Description', models.TextField(max_length=200)),
                ('File', models.ImageField(blank=True, upload_to='todo/')),
                ('WorkDone', models.BooleanField(null=True)),
                ('Checked', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserReg',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='auth.user')),
                ('Username', models.CharField(max_length=20, verbose_name='用户')),
                ('Email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('Password', models.CharField(max_length=20, verbose_name='密码')),
                ('Password2', models.CharField(max_length=20, verbose_name='重复密码')),
                ('Birthday', models.DateField(default='yyyy/mm/dd', null=True)),
                ('Position', models.CharField(choices=[('MG', 'Manager'), ('EG', 'Engineer'), ('MN', 'Monitor'), ('Wk', 'Worker')], default='Wk', max_length=2)),
                ('Date_Joined', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]