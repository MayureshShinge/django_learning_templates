#importing path and views for mapping urls
from django.urls import path

from . import views

#this is where we specify mapping
#TEMPLATE TAGGING

app_name = 'basic_app'

urlpatterns = [
    path('', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]