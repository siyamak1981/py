from django.db import models

# Create your models here.

class Roles:
    title = models.CharField(max_length =32)
    description = models.TextField()


class Bosses:
    role = models.ForeignKey('Roles', on_delete = models.PROTECT, related_name='boss')
    city = models.ForeignKey('City', on_delete = models.PROTECT, related_name='boss')
    


class City:
    title = models.CharField(max_length =32)
    province = models.CharField(max_length =32)
