from django.conf.urls import patterns, include, url
from views import *

from rest_framework import routers
from rest_quickstart import views

from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),

    # URLs for User authentication and Registration
    url(r'login/', Login.as_view()),
    url(r'logout/', Logout.as_view()),
    url(r'user-registration/', UserRegister.as_view()),
    url(r'api/', include(router.urls)),
    url(r'^api-urls', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^snippets/', include('snippets.urls')),
)
