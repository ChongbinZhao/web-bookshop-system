from django.db import models

# Create your models here.


# 出版社类
class Publisher(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('名称', max_length=64)
    addr = models.CharField('地址', max_length=64)


# 书籍的类
class Book(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('名称', max_length=64, null=True)
    ISBN = models.CharField('编号', max_length=64)
    translator = models.CharField('译者', max_length=64)
    date = models.DateField('出版日期', max_length=64,blank=True)
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE)  # Django中创建外键联表操作


# 作者的类
class Author(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('姓名', max_length=64)
    sex = models.CharField('性别', max_length=4)
    age = models.IntegerField('年龄', default=0)
    tel = models.CharField('联系方式', max_length=64)
    # 一个作者可以对应多本书，一本书也可以有多个作者，多对多，在数据库中创建第三张表
    book = models.ManyToManyField(to=Book)


# 用户的类
class LmsUser(models.Model):
    id = models.AutoField('序号', primary_key=True)
    username = models.CharField('用户名', max_length=32)
    password = models.CharField('密码', max_length=32)
    email = models.CharField('邮箱', max_length=254)
    mobile = models.BigIntegerField('手机',blank='True')
