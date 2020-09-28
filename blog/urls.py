from django.urls import path
from . import views
from .views import post_list

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
