"""Test App Urls."""
from django.conf import settings
from django.urls import include, path, re_path
from rest_framework import routers
from knox import views as knox_views
from TestApp.views.api.register import RegisterAPI
from TestApp.views.api.login import LoginAPI

router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = [
    path('v1/', include((router.urls, 'api_views'), )),
    path('v1/register/', RegisterAPI.as_view(), name='register'),
    path('v1/login/', LoginAPI.as_view(), name='login'),
]
