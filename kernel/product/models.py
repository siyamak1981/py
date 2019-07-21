from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from painless.models import choices as options
from painless.models.mixins import OrganizedMixin
from painless.models.mixins import TimeStampedMixin

status = options.PostStatus(is_charfield = False)
class Size(OrganizedMixin):
    SHIRT_SIZE = (
        ('xS', 'XtraSmall'),
        ('S','Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'XtraLarge'),
    )
    class Meta:
        ordering = ('title',)
        verbose_name = 'size'
        verbose_name_plural = 'sizes'
        
class ProductCatalog(OrganizedMixin):
    # picture = models.ManyToManyField(Image, null = True, blank = True, on_delete = models.CASCADE )
    price = models.DecimalField(default='0.0', max_digits=10, decimal_places=2)
    content = models.TextField()
    # shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZE)
    # size = models.ForeignKey('FIlter', on_delete=models.PROTECT)
    COLOR_CHOICES =(
        (u'blue', 'blue'),
        (u'green', 'green'),
        (u'red', 'red')
    )
    color_choices = models.CharField(max_length=1, choices=COLOR_CHOICES)
    status = models.PositiveSmallIntegerField(choices = status.get_status(), default = status.DRAFT)
    published_at = models.DateTimeField(default=timezone.now())    
    banner = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('created',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        get_latest_by = ['-published_at']
        
class ProductType(OrganizedMixin):
    productID = models.ForeignKey('ProductCatalog', on_delete = models.CASCADE,)
    typeTitle = models.CharField(max_length=200)


class Product_subType(OrganizedMixin):
    typeID = models.ForeignKey('ProductType', on_delete = models.CASCADE,)
    subType_title = models.CharField(max_length=200 , null=False, blank=False)    