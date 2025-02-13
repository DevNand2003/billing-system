from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    



    path('', views.create_bill, name='create_bill'),
    path('search/', views.search_bill, name='search_bill'),

]