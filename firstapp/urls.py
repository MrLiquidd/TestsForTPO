from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('about/', views.about, name='about'),
    path('main/', views.post_list, name='post_list'),
    path('list/', views.readPost, name='index_list'),
    path('list/search', views.search, name='search_list'),
    path('list/create', views.createPost, name='create'),
    path('update/<int:id>', views.updatePost, name='update'),
    path('list/delete/<int:id>', views.deletePost, name='delete'),
    path('list/client', views.readClient, name='client_list'),
    path('list/create_client', views.createClient, name='create_client'),
    path('client/update/<int:id>', views.updateClient, name='update_client'),
    path('client/delete/<int:id>', views.deleteClient, name='delete_client'),
    path('login/', views.user_login, name='login'),
    path('registr/', views.registr, name='registr'),
    path('mainproject/', views.mainproject, name='mainproject'),
    path('mainproject/test/', views.test, name='test'),
    path('map/', views.map, name='map')

]
