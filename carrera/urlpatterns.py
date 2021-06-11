#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：carrera 
@File    ：urlpatterns.py
@Author  ：宇宙大魔王
@Date    ：2021/6/11 15:50 
@Desc    ：
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from utils.token.handler import APITokenObtainPairView

conf_urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title="drf docs")),
]

common_urlpatterns = [
    path('login/', APITokenObtainPairView.as_view(), name='token_obtain_pair'),
]

api_urlpatterns = [
    path('', include(common_urlpatterns)),
    path('', include(conf_urlpatterns)),
]
