from . import views
from django.conf.urls import re_path

app_name = 'user_app'

urlpatterns = [
    re_path(r'^register/$', views.register, name="register"),
    re_path(r'^login/$', views.login_user, name="login"),
    
]