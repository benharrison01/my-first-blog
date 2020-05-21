from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.homepage, name='homepage'),
    path("post_list", views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('my_cv/', views.my_cv, name='my_cv'),
    path('contact/', views.contact, name='contact'),
    path('useful_links/', views.useful_links, name='useful_links'),
]
