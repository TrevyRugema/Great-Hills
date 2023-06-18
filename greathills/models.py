from distutils.command.upload import upload
from email.mime import image
from importlib.resources import contents
from site import venv
from tabnanny import verbose
from turtle import title
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class ContactTable(models.Model):
    FullName = models.CharField(max_length = 200)
    EmailAddress = models.CharField(max_length= 200)
    Subject = models.CharField(max_length = 200)
    Message = models.TextField()

    class Meta:
        verbose_name ="Subject"
        verbose_name_plural = "Subject"
    
    def __str__(self):
        return self.Subject 

class LatestEvents(models.Model):
    photo = models.ImageField(upload_to='images')
    title = models.CharField(max_length = 100)
    posted_date = models.DateField()
    author = models.CharField(max_length=100)
    contente_title = RichTextField( blank=True, null=100)
    contents = RichTextUploadingField( blank=True, null=500)

    class Meta: 
        verbose_name = "Lastest_Events"
        verbose_name_plural ="Lastest_Events"

    def __str__(self):
        return self.title

class FutureEvents(models.Model):
    upload_photo = models.ImageField(upload_to='images')
    title = models.CharField(max_length = 100)
    posted_date = models.DateField()
    author = models.CharField(max_length = 100)
    content_title = RichTextField( blank=True, null=100)
    big_contents = RichTextUploadingField( blank=True, null=500)

    class Meta:
        verbose_name = "Future_Events"
        verbose_name_plural ="Future_Events"

    def __str__(self):
        return self.title
        

