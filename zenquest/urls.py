from django.urls import path
from . import views

urlpatterns = [
    path('', views.technology, name='technology'),
    path('2/', views.t2, name='t2'),
    path('1/', views.t1, name='t1'),
]
