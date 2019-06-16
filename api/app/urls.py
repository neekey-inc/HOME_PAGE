
from django.conf.urls import include, url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import ArticleViewSet, NewsViewSet, UserViewSet, UserInfoViewSet
from rest_framework import routers

router = DefaultRouter()
# router.register(r'article', ArticleViewSet)
# router.register(r'news', NewsViewSet)
# router.register(r'user/sign', UserViewSet)
# router.register(r'user', UserInfoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
