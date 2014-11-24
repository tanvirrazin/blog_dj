from django.conf.urls import patterns, url
from blog.views import *


urlpatterns = patterns('',
    url(r'^$', AllBlogs.as_view()),
    url(r'^all/', AllBlogs.as_view()),
    url(r'^view/(?P<article_id>\d+)/', SingleBlog.as_view()),
    url(r'^like/(?P<article_id>\d+)/', LikeArticle.as_view()),
    url(r'^create/', CreateArticle.as_view()),
    url(r'^create-comment/(?P<article_id>\d+)$', CreateComment.as_view()),
)
