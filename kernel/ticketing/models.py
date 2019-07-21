from django.db import models
from presureless.choices import TicketStatus
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.core.validators import FileExtensionValidator
# Create your models here.
from presureless import choices as options
status = options.TicketStatus(is_charfield = False)


class Message(models.Model):
    title = models.CharField(max_length = 128)
    description = models.TextField( blank = True, null = True )
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    answer = models.ForeignKey("self", null = True, blank = True, on_delete = models.SET_NULL)
    ticket = models.ForeignKey("Ticketing", on_delete = models.CASCADE, related_name = 'message')

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
    
    def __str__(self):
        return self.title

class Department (models.Model):
    title = models.CharField(max_length = 128)
    description = models.TextField( blank = True, null = True )  

    class Meta:
        verbose_name = 'department'
        verbose_name_plural = 'departments'
    
    def __str__(self):
        return self.title

    
class Ticketing(models.Model):
    start_date = models.DateField()
    expire_date = models.DateField()
    severity = models.PositiveIntegerField(unique = True)
    # Level (basic, normal, pro, advance, master)
    status = models.PositiveSmallIntegerField(choices = status.get_status(), default = status.CLOSE)
    department = models.ForeignKey("Department" , on_delete = models.CASCADE, related_name='ticket')
    

    class Meta: 
        ordering = ['-start_date', 'expire_date', 'severity', 'status']
        verbose_name = 'ticket'
        verbose_name_plural = 'tickets'
        
    
    def __str__(self): 
        return self.severity
    
class Attachment(models.Model):
    title = models.CharField(max_length = 128)
    attachment = models.FileField(upload_to = 'tickets', 
                                    validators=[FileExtensionValidator(['docx', 'doc', 'pdf', 'jpg', 'png'])], 
                                    help_text = 'supported files: doc, pdf, jpg, png and docx')

    ticket = models.ForeignKey("Ticketing", on_delete = models.CASCADE, related_name = 'attachment')

    class Meta:
        verbose_name = 'attachment'
        verbose_name_plural = 'attachments'
    
    def __str__(self):
        return self.title
    