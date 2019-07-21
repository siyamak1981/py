from django.contrib import admin
from khayyam import JalaliDate as jd

from . import models

# Register your models here.


@admin.register(models.Ticketing)
class TicketingAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    pass
