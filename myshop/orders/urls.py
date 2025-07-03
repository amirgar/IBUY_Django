from . import views
from django.urls import re_path 


urlpatterns = [
    re_path(r'^create/$', views.order_create, name='order_create'),
]