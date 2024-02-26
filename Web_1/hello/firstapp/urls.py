from django.urls import path
from django.urls import re_path
from .import views

urlpatterns = [
    re_path(r'^contact', views.contact),
    re_path(r'^about', views.about),
    # re_path(r'^products/$', views.products),  # маршрут по умолчанию
    path('products/', views.products), # маршрут по умолчанию
    # re_path(r'^products/(?P<productid>\d+)/', views.products),
    path('products/<int:productid>/', views.products),
    path('users/', views.users), # маршрут по умолчанию
    # re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
    path('users/<int:id>/<name>/', views.users),
    path('details', views.details),
    path('', views.index),
    path('access/<int:age>/', views.access),

]