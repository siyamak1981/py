import uuid
import secrets

from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from painless.models import choices as options
from painless.models.mixins import OrganizedMixin
from painless.models.mixins import TimeStampedMixin
# from coleman.ratings.models import Rating

status = options.PostStatus(is_charfield = False)
class Category(OrganizedMixin):
    class Meta:
        ordering = ['-created']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        # return self.name
        return self.title

class Product(TimeStampedMixin):
    # sku = models.CharField(primary_key = True, default =secrets.toekn_urlsafe(15), max_lenth = 32, editable = False)
    name = models.CharField(max_length = 128, unique_for_month='published_at', help_text = 'must be unique')
    slug = models.CharField(max_length = 128, unique_for_month='published_at')
    banner = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    content = models.TextField(blank=True)
    summary = models.CharField(max_length = 128)
    price = models.DecimalField(default='0.0', max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
   
    
    status = models.PositiveSmallIntegerField(choices = status.get_status(), default = status.DRAFT)
    published_at = models.DateTimeField(default=timezone.now())
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    
    
    class Meta:
        ordering = ['-published_at', 'name']
        verbose_name = 'product'
        verbose_name_plural = 'products'
        get_latest_by = ['-published_at']
    

    def __str__(self):
        return self.name

class ProductType(models.Model):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False )
    name = models.CharField(max_length = 128)
    description = models.TextField()
    product=models.ForeignKey(Product,  on_delete=models.CASCADE , related_name='+') 
    
    
    class Meta:
        verbose_name = 'product-type'
        verbose_name_plural = 'product-types'
        

    def __str__(self):
        return self.name

class ProductTypeAttr(models.Model):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    fk_product_type = models.ForeignKey("ProductType",related_name='+', on_delete = models.CASCADE)
    fk_product_attr = models.ForeignKey("Attributes", related_name='+', on_delete = models.CASCADE)

class Attributes(models.Model):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length = 128)
    description = models.TextField()
    productattrvalue = models.ManyToManyField(Product, related_name = 'attrvalue')
    
class AttrValues(models.Model):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    fk_attr = models.ForeignKey("Attributes",related_name='+', on_delete = models.CASCADE)
    name = models.CharField(max_length = 128)
    description = models.TextField()



# class Rating(models.Model):
#     rating = models.IntegerField() 
#     content_type = models.ForeignKey(ContentType)
#     object_id = models.PositiveIntegerField()
#     content_object = generic.GenericForeignKey('content_type','object_id') 

# https://github.com/wildfish/django-star-ratings
# pip install django-star-ratings
# url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
# {% load static %}
# <html>
# ...
# <link rel="stylesheet" href="{% static 'star-ratings/css/star-ratings.css' %}">
# <script type="text/javascript" src="{% static 'star-ratings/js/dist/star-ratings.min.js' %}"></script>
# ...
# </html>
# {% extends "star_ratings/widget_base.html" %}
# {% block rating_detail %}
# Whatever you want
# {% endblock %}


# {% load ratings %}
# <html>
# ...
# {% ratings object %}
# ...
# </html>


# {% extends "star_ratings/widget_base.html" %}
# {% block rating_detail %}
# Whatever you want
# {% endblock %}



# from django.contrib.contenttypes.fields import GenericRelation
# from star_ratings.models import Rating

# class Foo(models.Model):
#     bar = models.CharField(max_length=100)
#     ratings = GenericRelation(Rating, related_query_name='foos')

# Foo.objects.filter(ratings__isnull=False).order_by('ratings__average')


# /myapp/models.py

# class MyRating(AbstractBaseRating):
#    foo = models.TextField()



# ./settings.py

# ...
# STAR_RATINGS_RATING_MODEL = 'myapp.MyRating'
# ...



# class MyRating(AbstractBaseRating):
#    object_id = models.CharField(max_length=10)