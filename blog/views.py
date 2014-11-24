from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import View
from django.core.context_processors import csrf
import datetime
import os
from blog.forms import CreateArticleForm, CreateCommentForm
from blog.models import *


app_tpl_dir = 'blog'


# Shows all Articles of all categories
class AllBlogs(View):

    def get(self, request):
        article_types = ArticleType.objects.all()
        for ind, article_type in enumerate(article_types):
            article_types[ind].articles = Article.objects.filter(type=article_type.id)

        user = request.user

        return render_to_response(os.path.join(app_tpl_dir, 'index.html'), {'user': user, 'article_types': article_types})


# Shows a single Article
class SingleBlog(View):

    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        article.likes = Like.objects.filter(article_id=article_id)
        article.comments = Comment.objects.filter(article_id=article_id)

        comment_form = CreateCommentForm()
        user = request.user

        args = {
            'user': user,
            'article': article,
            'comment_form': comment_form
        }
        args.update(csrf(request))

        return render_to_response(os.path.join(app_tpl_dir, 'single_blog.html'), args)


# Counts like for an Article
class LikeArticle(View):

    def get(self, request, article_id):
        new_like = Like(article_id=article_id, user_id=request.user.id)
        new_like.save()

        return HttpResponseRedirect('/blog/view/%s' % article_id)


class CreateArticle(View):

    def get(self, request):
        form = CreateArticleForm()

        args = {}
        args.update(csrf(request))
        args['form'] = form
        args['user'] = request.user

        return render_to_response(os.path.join(app_tpl_dir, 'create_article_form.html'), args)

    def post(self, request, *args, **kwargs):
        form = CreateArticleForm(request.POST)

        if form.is_valid:
            article = form.save(commit=False)
            article.pub_date = datetime.datetime.now()
            article.user = request.user
            article.save()
        return HttpResponseRedirect('/blog/')


class CreateComment(View):

    def post(self, request, article_id):
        print request.POST
        new_comment = CreateCommentForm(request.POST)
        if new_comment.is_valid():
            comment = new_comment.save(commit=False)
            comment.user = request.user
            comment.article = Article.objects.get(id=article_id)
            comment.save()
        return HttpResponseRedirect('/blog/view/'+article_id)