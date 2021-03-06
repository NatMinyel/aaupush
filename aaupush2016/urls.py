"""aaupush2016 URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url , include
from django.contrib import admin
from main import views
urlpatterns = [
    url(r'^$' ,views.index, name='Home'),
    url(r'^section/', include('main.urls')),
    url(r'^file/(?P<material_id>[0-9a-zA-Z]+)/$',views.file_view, name='File'),
    url(r'^login/$',views.login_view, name='login'),
    url(r'^backend/$',views.backend_view, name='backend_view'),
    url(r'^portal/$',views.portal, name='portal'),
    url(r'^first_login/$',views.first_login, name='first_login'),
    url(r'^admin/', admin.site.urls),
]
