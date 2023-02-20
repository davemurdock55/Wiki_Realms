from django.db import models

# Used to connect any table to any other table generically
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class MediaProject(models.Model):
     name = models.CharField(max_length=100, blank=False, null=False)
     description = models.CharField(max_length=255, blank=True, null=True)
     media_project_image = models.ImageField(upload_to='images/', blank=True, null=True)
     publish_date = models.DateField(blank=True, null=True)

     def __str__(self):
          return self.name


class WikiPage(models.Model):
     users = models.ManyToManyField(to='main.Profile')
     realm = models.ForeignKey(to='worldbuilding.Realm', on_delete=models.CASCADE, blank=False, null=False)
     
     title = models.CharField(max_length=100, blank=False, null=False)
     header_image = models.ImageField(upload_to='images/', blank=True, null=True)
     subheading = models.CharField(max_length=100, blank=True, null=True)
     description = models.CharField(max_length=255, blank=True, null=True)
     text = models.TextField(blank=True, null=True)
     # We could give wiki_pages a "type" field that will have certain choices that will automatically be ticked
     # by the program whenever a wiki page is created based on the type of worldbuilding page it is based on.
     # type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=)

     def __str__(self):
          return self.name
