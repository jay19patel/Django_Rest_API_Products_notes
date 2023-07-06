from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeAPI, name="HomeAPI") , 
    path('get/', views.GetAPI, name="GetAPI") , 
    path('getone/<str:id>/', views.GetOneAPI, name="GetOneAPI") , 
    path('post/', views.PostAPI, name="PostAPI") , 
]