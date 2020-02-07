from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class ArticlePost(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE) #ForeignKey一对多
    title=models.CharField(max_length=100)
    body=models.TextField()
    created=models.DateTimeField(default=timezone.now)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('-created',)    #倒序排列
    def __str__(self):
        return self.title
