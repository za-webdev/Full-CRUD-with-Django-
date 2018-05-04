from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.main),
	url(r'^index$',views.index),
	url(r'^create$',views.create),
	url(r'^remove/(?P<user_id>\d+)$',views.remove),
	url(r'^show/(?P<user_id>\d+)$',views.show),
	url(r'^edit/(?P<user_id>\d+)$',views.edit),
	url(r'^edit_here/(?P<user_id>\d+)$',views.edit_here),

]