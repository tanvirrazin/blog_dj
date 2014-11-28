from django.conf.urls import url, patterns
from api.views import *


urlpatterns = patterns('',
    url(r'^article-types/', ArticleTypeList.as_view()),
)