from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^index/$', views.shell, name='shell'),
	url(r'^index/(?P<group_id>\d+)/$', views.shell, name='shell')
]
