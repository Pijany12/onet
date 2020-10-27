from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('login/', views.login),
	path('test/', views.test),
	path('fb-login/', views.fb_login),
	path('*/(?P<path>.*)$', views.redirect),
]