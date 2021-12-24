from django.conf.urls import url
from basic_app import views

#TEMPLATE_TAGGING
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$', views.realtive, name='relative'),
    url(r'^other/$', views.other, name='other'),
]
