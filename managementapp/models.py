from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.admin.widgets import AdminDateWidget
from django.dispatch import receiver
import datetime

# Create your models here.
class UserReg(models.Model):
    #add attribute to user model by using one to one field
    Id = models.OneToOneField(User, on_delete=models.DO_NOTHING, primary_key=True)
    Position_Choices = [('Manager','Manager'),('Engineer','Engineer'),('Monitor','Monitor'),('Worker','Worker')]
    Username = models.CharField('用户', max_length=20)
    Email = models.EmailField('邮箱')
    Password = models.CharField('密码', max_length=20)
    Password2 = models.CharField('重复密码', max_length=20)
    Birthday = models.DateField(null=True, default='yyyy/mm/dd')
    Position = models.CharField(max_length=15, choices=Position_Choices, default='Worker')
    Date_Joined = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.Username

    def __unicode__(self):
        return self.Id




class Todo(models.Model):
    Assign_By = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default='1')
    Assign_Time = models.DateTimeField(auto_now_add=True, null=True)
    Work = models.CharField(max_length=200)
    Description = models.TextField(max_length=200)
    Assign = models.ManyToManyField(UserReg)
    File = models.ImageField(blank=True, upload_to='todo/')
    WorkDone = models.BooleanField(null=False, default=False)
    Checked = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.Work



class Signin(models.Model):
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
