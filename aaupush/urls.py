"""aaupush URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^section/(?P<section_code>[0-9a-zA-Z]+)/$', views.section_view, name='section'),
    url(r'^materials/(?P<section_code>[0-9a-zA-Z]+)/(?P<folder_link_name>[0-9a-zA-Z-]+)/$', views.folder_view, name = 'folder'),
    url(r'^file/(?P<material_id>[0-9]+)/$', views.file_view, name='file'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^portal/$', views.portal_view, name='portal'),
    url(r'^backend/$', views.backend_view, name='backend'),
    url(r'^admin/', admin.site.urls),
]
