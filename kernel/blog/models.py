import uuid
import secrets
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from painless.models import choices as options
from painless.models.mixins import OrganizedMixin
from painless.models.mixins import TimeStampedMixin
from painless.models.managers import PostPublishedManager

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
    

    objects = models.Manager()
    condition = PostPublishedManager()

    class Meta:
        ordering = ['-published_at', 'title']
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        get_latest_by = ['-published_at']

    def __str__(self):
        return self.title

# class Comment(TimeStampedModel):
#     commented_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
#     for_post = models.ForeignKey(Post, related_name='comments', on_delete = models.CASCADE)
#     parent = models.ForeignKey("self", null = True, blank = True, on_delete = models.SET_NULL)
#     content = models.TextField()
#     status = models.PositiveSmallIntegerField(choices=opt_status.get_status(), default = opt_status.PUDBLISHED)

#     class Meta:
#         ordering = ['-created']
#         verbose_name = 'comment'
#         verbose_name_plural = 'comments'
    
    
#     def __str__(self): 
#         return self.for_post.title




class Comment(TimeStampedMixin):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    title = models.CharField(max_length= 128, unique = True)
    email = models.EmailField()
    content = models.TextField()
    active = models.BooleanField(default=True)
    reply_to = models.ForeignKey('self',null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    class Meta:
        ordering = ('created',)
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        get_latest_by = ['-created']

    def __str__(self):
        return 'Comment by {} on {}'.format(self.title, self.post) 