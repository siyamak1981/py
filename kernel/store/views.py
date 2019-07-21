

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from .models import Product
class ShopListView(ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'shop'

