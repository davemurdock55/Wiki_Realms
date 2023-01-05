from django.db import models

# Used to connect any table to any other table generically
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Realm(models.Model):
     name = models.CharField(max_length=100)
     description = models.CharField(max_length=255)
     image = models.ImageField(upload_to='images/')

     def __str__(self):
          return self.name


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    WORLDBUILDING PAGE MODELS    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

class Page(models.Model):
     users = models.ManyToManyField(to='User')
     realm = models.ForeignKey(to='Realm', on_delete=models.CASCADE)
     
     name = models.CharField(max_length=100)
     description = models.CharField(max_length=255)
     header_image = models.ImageField(upload_to='images/')


     def __str__(self):
          return self.name

class PlotArc(Page):
     media_project = models.ForeignKey(to='MediaProject', on_delete=models.SET_NULL)


class PlotPoint(Page):
     # The question is, do we want a plotpoint to NEED/Be dependent on a PlotArc existing?
     plot_arc = models.ForeignKey(to='PlotArc', on_delete=models.SET_NULL)
     setting = models.ForeignKey(to='Setting', on_delete=models.SET_NULL)

     pages = models.ManyToManyField(to='Page')
     characters = models.ManyToManyField(to='Character')
     items = models.ManyToManyField(to='Item')
     magic_systems = models.ManyToManyField(to='Magic')
     social_structures = models.ManyToManyField(to='SocialStructure')

     # I think I want plot_progression to be able to be negative...?
     plot_progression = models.SmallIntegerField()
     

class Character(Page):
     # can be negative or positive
     development = models.SmallIntegerField()



class Setting(Page):
     encompassing_setting = models.ForeignKey(to='Setting', on_delete=models.SET_NULL)


class Item(Page):
     pass


class Magic(Page):
     pass


class SocialStructure(Page):
     pass


class CharacterRelationship(models.Model):
     # idk if this is the best way to do this!!!
     character1 = models.ForeignKey(to='Character', on_delete=models.CASCADE, related_name='character1')
     character2 = models.ForeignKey(to='Character', on_delete=models.CASCADE, related_name='character2')

     type = models.CharField(max_length=50)
     description = models.CharField(max_length=255)
     strength = models.PositiveSmallIntegerField()
     
     def __str__(self):
          return self.name


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    CONTENT BLOCK MODELS    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

class Text(models.Model):
     page = models.ForeignKey(to='Page', on_delete=models.CASCADE)

     name = models.CharField(max_length=100)
     text = models.TextField()
     
     def __str__(self):
          return self.name


class Image(models.Model):
     page = models.ForeignKey(to='Page', on_delete=models.CASCADE)

     name = models.CharField(max_length=100)
     image = models.ImageField(upload_to='images/')

     def __str__(self):
          return self.name


class Graph(models.Model):
     page = models.ForeignKey(to='Page', on_delete=models.CASCADE)

     name = models.CharField(max_length=100)
     x_label = models.CharField(max_length=100)
     y_label = models.CharField(max_length=100)
     data = models.JSONField()
     
     def __str__(self):
          return self.name


class CharacterWeb(models.Model):
     page = models.ForeignKey(to='Page', on_delete=models.CASCADE)

     name = models.CharField(max_length=100)
     # image = models.ImageField(upload_to='images/') # this was automatically created by co-pilot
     description = models.CharField(max_length=255)

     # this was automatically created by co-pilot
     relationships = models.ManyToManyField(to='CharacterRelationship')
     
     def __str__(self):
          return self.name


class Map(models.Model):
     page = models.ForeignKey(to='Page', on_delete=models.CASCADE)
     # setting = models.ForeignKey(to='Setting', on_delete=models.SET_NULL, default=None, null=True)

     name = models.CharField(max_length=100)
     image = models.ImageField(upload_to='images/')
     
     def __str__(self):
          return self.name


class Pin(models.Model):
     page = models.ForeignKey(to='Page', on_delete=models.CASCADE)
     map = models.ForeignKey(to='Map', on_delete=models.CASCADE)

     # Supposedly, these next three lines should allow the "name" field to come from the "name"field of any other model in the database???
     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
     object_id = models.PositiveIntegerField()
     name = GenericForeignKey('content_type', 'object_id')

     description = models.CharField(max_length=255)
     
     # You will need to edit this icon field to be more of an SVG choice
     icon = models.ImageField(upload_to='images/')
     x = models.PositiveSmallIntegerField()
     y = models.PositiveSmallIntegerField()
     
     def __str__(self):
          return self.name


class Region(models.Model):
     page = models.ForeignKey(to='Page', on_delete=models.CASCADE)
     map = models.ForeignKey(to='Map', on_delete=models.CASCADE)
     region_type = models.ForeignKey(to='RegionType', on_delete=models.CASCADE)

     # We want this to come from the Setting, Magic, or SocialStructure
     # name = models.ForeignKey(max_length=100)

     # Supposedly, these next three lines should allow the "name" field to come from the "name"field of any other model in the database???
     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
     object_id = models.PositiveIntegerField()
     name = GenericForeignKey('content_type', 'object_id')
     
     # From the Django GEO API. This is supposed to be a polygon field that can be drawn on the map
     shape = models.GeometryField()


     def __str__(self):
          return self.name


# This is supposed to be a reference table for Regions so that we can standardize and protect the data from errors
class RegionType(models.Model):
     region_type_name = models.CharField(max_length=100)

     def __str__(self):
          return self.region_type_name


