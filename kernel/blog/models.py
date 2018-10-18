import uuid
import secrets
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from painless.models import choices as options
from painless.models.mixins import OrganizedMixin
from painless.models.mixins import TimeStampedMixin

status = options.PostStatus(is_charfield = False)
# Create your models here.
class Tag(OrganizedMixin):
    class Meta:
        ordering = [ '-created' ]

    def __str__(self):
        return self.title
 

class Category(OrganizedMixin):
    class Meta:
        ordering = ['-created']
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):

        return self.title

class Post(TimeStampedMixin):
    uid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length = 128, unique_for_month='published_at', help_text = 'must be unique')
    slug = models.CharField(max_length = 128, unique_for_month='published_at')
    banner = models.ImageField(upload_to = 'blog', null = True, blank = True)
    summary = models.CharField(max_length = 128)
    content = models.TextField()
    status = models.PositiveSmallIntegerField(choices = status.get_status(), default = status.DRAFT)
    # status = models.PositiveSmallIntegerField(choices = POST_STATUS, default = DRAFT)


    tag = models.ManyToManyField('Tag', related_name = 'post')
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'posts')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name = 'posts')


    published_at = models.DateTimeField(default=timezone.now())
    


    class Meta:
        ordering = ['-published_at', 'title']
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        get_latest_by = ['-published_at']

    def __str__(self):
        return self.title