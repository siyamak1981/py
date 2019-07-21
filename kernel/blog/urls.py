from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('posts/', views.PostListView.as_view(), name = 'posts'),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name = 'post'),
    path('bosses/', views.BossListView.as_view(), name = 'bosses'),
    path('boss/example/', views.BossDetailView.as_view(), name = 'boss'),


]