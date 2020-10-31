from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('tags/<int:pk>/', views.tag, name='tag'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
]
