from django.test import TestCase
from django.utils import timezone
# Create your tests here.
from .models import Post
from .models import Category
from django.contrib.auth.models import User


class PostModelsTest(TestCase):
    def setUp(self):
        category =Category.objects.create(
            title ="python",
            slug = "python-django"
        )
        self.user1 = User.objects.create(
            username = "siyamak",
            email = "siyamak1981@gmail.com",
            password = "siyamak1981",

        )
        
        self.user2 =User.objects.create(
            username = "saed",
            email = "saed@gmail.com",
            password = "123456",

        )


    def test_post_creation(self):
        post = Post(
            title = "this is a great title",
            slug = 'sport-news',
            content = "some great msg",
            banner = None,
            Category = None,

         )

        post.auther.add(self.user1)
        post.author.add(self.user2)
        post.save()

        self.assertLess(post.published_at, timezone.now())


class PostViewTest(TestCase):
    def setUp(self):
        category =Category.objects.create(
            title ="python",
            slug = "python-django"
        )
        self.user1 = User.objects.create(
            username = "siyamak",
            email = "siyamak1981@gmail.com",
            password = "siyamak1981",

        )
        
        self.user2 =User.objects.create(
            username = "saed",
            email = "saed@gmail.com",
            password = "123456",

        )
        
        self.post = Post(
            title = "this is a great title",
            slug = 'sport-news',
            content = "some great msg",
            banner = None,
            Category = None,

         )

        self.post.auther.add(self.user1)
        self.post.author.add(self.user2)
        self.post.save()

        
    def test_post_list_view(self):
        resp = self.client.get(reverse('list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.post, resp.context['posts'])
        self.assertTemplateUsed(resp, 'blog/post_list.html')

    def test_post_detail_view(self):
        resp = self.client.get(reverse('detail', kwargs ={'uid' =self.post.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.post, resp.context['post'])
        self.assertTemplateUsed(resp, 'blog/post.html')
        self.assertContains(resp, self.post.title)
