from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True)

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets',)