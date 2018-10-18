from django.contrib import admin
from .models import Post
from .models import Tag
from .models import Category
from khayyam import JalaliDate as jd
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_published', 'published', 'category', 'get_tags']
    prepopulated_fields = { "slug": ('title',)}
    prepopulated_fields = { "slug": ('title',)}
    list_editable = ['category']
    list_filter = ['status', 'published_at', 'category__title']
    filter_horizontal = ['tag']
#     # fields = (
#     #     ('title', 'slug',),
#     #     ('status', 'category', 'author',),
#     #     'tag',
#     #     ('published_at', 'banner'),
#     #     'summary',
#     #     'content',
#     # )

    fieldsets = [
        ('main', { 
            'fields': ( 
                    ('title', 'slug'), 
                    ('author', 'status', 'category') 
                ),
            }
        ),

        ('Advanced_options', { 
            'fields': (
                    'tag',
                    'banner',
                    'summary',
                    'content',
                    'published_at',
                ),
            'classes': ('collapse',)
            },

        ),
    ]

    def published(self, obj):
        return jd(obj.published_at)

    def get_tags(self, obj):
        return ", ".join([t.title for t in obj.tag.all()])

    def is_published(self, obj):
        published = 1
        return obj.status == published
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return super().has_delete_permission(request)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('published_at',)
        return []

    is_published.boolean = True



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at', 'updated_at']
    list_filter = ['created',]
    prepopulated_fields = { "slug": ('title',)}
    search_fields = ['title']
    actions_on_bottom = True
    date_hierarchy = 'created'
    empty_value_display = '--empty--'
    
    def created_at(self, obj):
        return jd(obj.created)
    
    def updated_at(self, obj):
        return jd(obj.updated)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created', 'updated']
    prepopulated_fields = { "slug": ('title',)}

    

    

   


admin.site.site_header = "Siyamak Adminstration"
admin.site.site_title = "Siyamak site admin"
admin.site.index_title = "Welcome to Siyamak dashboard"

