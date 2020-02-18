from . import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('<slug:slug>/edit/', views.post_edit, name='post_edit'),

]
