from django.db import models

# Used to connect any table to any other table generically
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class MediaProject(models.Model):
     name = models.CharField(max_length=100)
     description = models.CharField(max_length=255)
     media_project_image = models.ImageField(upload_to='images/')
     publish_date = models.DateField()

     def __str__(self):
          return self.name


class WikiPage(models.Model):
     users = models.ManyToManyField(to='main.User')
     realm = models.ForeignKey(to='worldbuilding.Realm', on_delete=models.CASCADE)
     
     title = models.CharField(max_length=100)
     header_image = models.ImageField(upload_to='images/')
     subheading = models.CharField(max_length=100)
     description = models.CharField(max_length=255)
     text = models.TextField()
     # We could give wiki_pages a "type" field that will have certain choices that will automatically be ticked
     # by the program whenever a wiki page is created based on the type of worldbuilding page it is based on.
     # type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=)

     def __str__(self):
          return self.name
