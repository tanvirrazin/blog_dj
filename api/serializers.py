from rest_framework import serializers
from blog.models import ArticleType


class ArticleTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleType
        fields = ('id', 'name')