from django import forms
from blog.models import Article, Comment


class CreateArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'body', 'type',)


class CreateCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)