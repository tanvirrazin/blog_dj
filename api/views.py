from blog.models import ArticleType
from api.serializers import ArticleTypeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ArticleTypeList(APIView):
    """
    List all the ArticleTypes that users has defined.
    """
    def get(self, request, format=None):
        article_types = ArticleType.objects.all()
        serializer = ArticleTypeSerializer(article_types, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleTypeSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)