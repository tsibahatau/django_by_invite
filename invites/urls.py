from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.user_login, name='user_login'),
    url(r'^login', views.user_login, name='user_login'),
    url(r'^accounts/login*', views.user_login, name='user_login'),
    url(r'^logout$', views.user_logout, name='user_logout'),
    url(r'^createUser', views.create_user, name='create_user'),
    url(r'^.*$',views.user_login, name='user_login')
]