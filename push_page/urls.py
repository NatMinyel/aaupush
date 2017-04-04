from django.conf.urls import url , include
from . import views

urlpatterns = [
    url('^(?P<quick_page>[0-9]+)/$',views.push_page, name='Quick_Page'),
    ]
