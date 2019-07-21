# from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from django.http import HttpResponse 
from blog.models import Post
# Create your views here.
# def index(request):
#     return HttpResponse("hi siyamak")

# def details(request, id):
#     return HttpResponse("your id number is {}".format(id))

# def details2(request):
#     return HttpResponse("your id number is {}".format(request.GET["id"]))   
# def show_products(request):
#     posts=Post.objects.all()[:5]
#     context= {
#        "latest_posts": posts
#     }

#     return render(request, 'blog/products.html', context)


# def detail(request, title):
#     post = get_object_or_404(Post, title=title)
    
#     context = {
#         "post": post
#     }
#     return render(request, 'blog/product.html', context)
class PostListView(ListView):
    model= Post
    template_name= "blog/products.html"
    context_object_name = 'latest_posts'

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/product.html"
    context_object_name = 'latest_post'


class HomeView(TemplateView):
    template_name = 'mysite/landing.html'
    page_name = 'landing'


class PrductListView(ListView):
    template_name = 'mysite/product_new.html'
    page_name = 'product_new'