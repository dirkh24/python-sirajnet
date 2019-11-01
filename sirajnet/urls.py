from django.urls import path, include
from . import views

app_name = 'sirajnet'
urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result')
]