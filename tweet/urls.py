from . import views
from django.urls import path
urlpatterns = [
    path('', views.tweet_list, name = 'tweet_list'),
    path('create/', views.tweet_create, name = 'tweet_create'),
    path('delete/<int:tweet_id>/', views.tweet_delete, name = 'tweet_delete'),
    path('edit/<int:tweet_id>/', views.tweet_edit, name = 'tweet_edit'),
    path('register/', views.register, name = 'register'),
    path('search/', views.search_tweets, name = 'search'),
]