"""Test App Urls."""
from django.conf import settings
from django.urls import include, path, re_path
from rest_framework import routers
from TestApp.views.api.register import RegisterAPI

router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = [
    path('v1/', include((router.urls, 'api_views'), )),
    path('v1/register/', RegisterAPI.as_view(), name='register'),
]
