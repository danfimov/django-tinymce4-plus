"""test_tinymce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from filebrowser.sites import site

from django import VERSION
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include

from test_tinymce.views import TestCreateView, TestDisplayView


if VERSION < (4, 0):
    from django.conf.urls import url
else:
    from django.urls import re_path as url


urlpatterns = [
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/filebrowser/', site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^content/(?P<pk>\d+)/$', TestDisplayView.as_view(), name='display'),
    url(r'^$', TestCreateView.as_view(), name='create')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
