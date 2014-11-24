from django.contrib.auth.models import User
from django.db import models


class ArticleType(models.Model):
    name = models.CharField(max_length=100, default='')

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, default='')
    body = models.TextField()
    pub_date = models.DateTimeField()
    type = models.ForeignKey(ArticleType)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title


class Like(models.Model):
    article = models.ForeignKey(Article)
    user = models.ForeignKey(User)


class Comment(models.Model):
    article = models.ForeignKey(Article)
    body = models.TextField()
    user = models.ForeignKey(User)