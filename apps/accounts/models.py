from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    用户的基本信息表
    """
    name = models.CharField(max_length=30, null=True,
                            unique=True, verbose_name="姓名",
                            error_messages={
                                'unique': '姓名已经在系统中存在'
                            })
    email = models.EmailField(max_length=100, verbose_name="邮箱",
                              unique=True,
                              error_messages={
                                  'unique': '邮箱已经在系统中存在'
                              })

    avatar = models.ImageField(verbose_name='用户头像', upload_to='avatar/', null=True, blank=True)

    class Meta:
        db_table = 'users'
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
