from django.urls import path
from . import views
app_name="mysite"
urlpatterns=[
    path('', views.HomeView.as_view(), name = 'landing'),
    # path('product_n', views.ProductView.as_view(), name = 'product_new'),
    path('posts/', views.PostListView.as_view(), name="posts"),
    # # path('product_n/', views.details2, name ='product_new'),
    # path('product/<str:title>', views.detail, name = 'product'),
    # path('post/<slug:slug>', views.PostDetailView.as_view(), name="post"),
]