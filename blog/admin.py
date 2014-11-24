from django.contrib import admin
from blog.models import ArticleType, Article, Like, Comment

admin.site.register(ArticleType)
admin.site.register(Article)
admin.site.register(Like)
admin.site.register(Comment)
