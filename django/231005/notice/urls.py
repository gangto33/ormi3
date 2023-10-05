from django.urls import path
from . import views

urlpatterns = [
    path('', views.notice, name='notice'),
    path('free/', views.free, name='free'),
    path('free/<int:pk>/', views.post, name='post'),
    path('onenone/', views.onenone, name='onenone'),
    path('onenone/<int:pk>/', views.onenone1, name='onenone1'),
]
