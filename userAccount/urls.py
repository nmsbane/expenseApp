from django.conf.urls import include, url
from . import views

urlpatterns = [
    # url(r'^login/$', views.user_login, name='login')    
    
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.dashboard, name='dashboard'),
]

