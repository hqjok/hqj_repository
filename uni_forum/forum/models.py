from django.db import models

# Create your models here.


class UserInfo(models.Model):
    uid = models.AutoField(primary_key=True)
    user_picurl = models.CharField(max_length=128, null=True)
    user_name = models.CharField(max_length=32)
    user_sex = models.CharField(choices=((0, "男"), (1, "女"), ), max_length=8)
    user_occupation = models.CharField(max_length=8, choices=((0, "教师"), (1, "学生"), ))
    user_Id = models.CharField(max_length=32)
    user_passwd = models.CharField(max_length=32)
    user_email = models.CharField(max_length=64, null=True)
