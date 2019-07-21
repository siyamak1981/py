from django.views.generic import ListView, DetailView, TemplateView
from .models import Post
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

class BossListView(TemplateView):
    # model = Boss
    template_name = 'blog/boss_list.html'
    # context_object_name = 'booses'

class BossDetailView(TemplateView):
    # model = Post
    template_name = 'blog/boss_detail.html'
    # context_object_name = 'boss'

# class PrductListView(ListView):
#     template_name = 'mysite/product_new.html'
#     page_name = 'product_new'