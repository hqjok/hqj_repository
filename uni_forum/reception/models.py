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


class Alltype(models.Model):
    atid = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)


class ArticleType(models.Model):
    tid = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=32)
    from_type = models.ForeignKey("Alltype", to_field="atid", on_delete=models.CASCADE, null=True)


class Article(models.Model):
    aid = models.AutoField(primary_key=True)
    art_title = models.CharField(max_length=128)
    art_author = models.CharField(max_length=64)
    art_content = models.TextField()
    art_create_date = models.DateField(auto_now_add=True)
    art_last_date = models.DateField(auto_now=True)
    art_click_count = models.IntegerField(default=0)
    art_lift = models.IntegerField(default=0)
    art_comment = models.TextField(default={})
    art_image = models.ImageField(upload_to="images")
    articleType = models.ForeignKey("ArticleType", on_delete=models.CASCADE, to_field='tid')
    art_author_lift = models.ManyToManyField("UserInfo")