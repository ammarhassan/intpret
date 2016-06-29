from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'/shell/$', views.shell, name='shell')


]
