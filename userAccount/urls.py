from django.conf.urls import include, url
from . import views

urlpatterns = [
    # url(r'^login/$', views.user_login, name='login')    
    #(r'^accounts/login/$', custom_login),
    url(r'^login/$', views.custom_login, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^addAccount/$', views.add_account, name='add_account'),
    url(r'^addBalance/$', views.add_balance, name='add_balance'),
    url(r'^addTag/$', views.add_tag, name='add_tag'),
    url(r'^$', views.dashboard, name='dashboard'),
]

