from django.db import models

# Used to connect any table to any other table generically
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# import django GEO
from django.contrib.gis.db import models



# Create your models here.
class Realm(models.Model):
     users = models.ManyToManyField(to='main.Profile')
     name = models.CharField(max_length=100, blank=False, null=False)
     description = models.CharField(max_length=255, blank=True, null=True)
     image = models.ImageField(upload_to='images/', blank=True, null=True)

     def __str__(self):
          return self.name


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    WORLDBUILDING PAGE MODELS    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

class Page(models.Model):
     users = models.ManyToManyField(to='main.Profile')
     realm = models.ForeignKey(to='Realm', on_delete=models.CASCADE, blank=False, null=False)
     
     name = models.CharField(max_length=100, blank=False, null=False)
     description = models.CharField(max_length=255, blank=True, null=True)
     header_image = models.ImageField(upload_to='images/', blank=True, null=True)


     def __str__(self):
          return self.name

class PlotArc(Page):
     media_project = models.ForeignKey(to='wiki.MediaProject', on_delete=models.SET_NULL, blank=True, null=True)

     def __str__(self):
          return self.name + " (Plot Arc)"

class PlotPoint(Page):
     # Not sure if we want PlotPoint to inherit from page or not!


     # The question is, do we want a plotpoint to NEED/Be dependent on a PlotArc existing?
     plot_arc = models.ForeignKey(to='PlotArc', on_delete=models.SET_NULL, blank=True, null=True)
     # a plot point can only be in one setting (unless we want to change this to be many-to-many)
     backdrop = models.ForeignKey(to='Setting', related_name='backdrop', on_delete=models.SET_NULL, blank=True, null=True)

     pages = models.ManyToManyField(to='Page', related_name='pages')
     characters = models.ManyToManyField(to='Character', related_name='characters')
     items = models.ManyToManyField(to='Item', related_name='items')
     magic_systems = models.ManyToManyField(to='Magic', related_name='magic_systems')
     social_structures = models.ManyToManyField(to='SocialStructure', related_name='social_structures')

     # I think I want plot_progression to be able to be negative...?
     plot_progression = models.SmallIntegerField(blank=True, null=True)
     
     def __str__(self):
          return self.name + " (Plot Point)"

class Character(Page):
     # can be negative or positive
     overall_development = models.SmallIntegerField(blank=True, null=True)



class Setting(Page):
     encompassing_setting = models.ForeignKey(to='Setting', on_delete=models.SET_NULL, blank=True, null=True)


class Item(Page):
     pass


class Magic(Page):
     pass


class SocialStructure(Page):
     pass


class CharacterRelationship(models.Model):
     # idk if this is the best way to do this!!!
     character1 = models.ForeignKey(to='Character', related_name='character1', on_delete=models.CASCADE, blank=False, null=False)
     character2 = models.ForeignKey(to='Character', related_name='character2', on_delete=models.CASCADE, blank=False, null=False)

     type = models.CharField(max_length=50, blank=False, null=False)
     description = models.CharField(max_length=255, blank=True, null=True)
     strength = models.PositiveSmallIntegerField(blank=True, null=True)
     
     def __str__(self):
          return self.name


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# vvv    CONTENT BLOCK MODELS    vvv
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
class ContentBlock(models.Model):
     # the page that the content block is on. The content block will be deleted if the page is deleted
     page = models.ForeignKey(to='Page', on_delete=models.CASCADE, blank=False, null=False)


     def __str__(self):
          return self.name


class TextBlock(ContentBlock):
     name = models.CharField(max_length=100, blank=False, null=False)
     text = models.TextField(blank=True, null=True)


class ImageBlock(ContentBlock):
     name = models.CharField(max_length=100, blank=False, null=False)
     image = models.ImageField(upload_to='images/', blank=True, null=True)


class AliasBlock(ContentBlock):
     alias = models.CharField(max_length=100, blank=True, null=True)


class QualityBlock(ContentBlock):
     type = models.ForeignKey(to='QualityType', on_delete=models.SET_NULL, blank=True, null=True)
     # amounts can be of any number, positive or negative, or can be set to a percentage in case they are (this is the default)
     amount = models.SmallIntegerField(default=100, blank=True, null=True)
     
     

class QualityType(models.Model):
     # users should be able to add their own quality types to the database (removing them should only be available to the app's admins)
     name = models.CharField(max_length=100, blank=False, null=False)
     description = models.CharField(max_length=255, blank=True, null=True)
     amount_unit = models.CharField(max_length=50, default='percent', blank=True, null=True)


class CharacterBlock(ContentBlock):
     character = models.ForeignKey(to='Character', on_delete=models.CASCADE, blank=False, null=False)


class ItemBlock(ContentBlock):
     item = models.ForeignKey(to='Item', on_delete=models.CASCADE, blank=False, null=False)


class CharacterListBlock(ContentBlock):
     # a character list can have multiple characters and a character can be in multiple character lists
     characters = models.ManyToManyField(to='Character', related_name='characters_in_character_list')
     
     name = models.CharField(max_length=100, blank=True, null=True)
     
class GoalBlock(ContentBlock):
     name = models.CharField(max_length=100, blank=False, null=False)
     description = models.CharField(max_length=255, blank=True, null=True)

     # amounts can be of any number, positive or negative, or can be set to a percentage in case they are (this is the default)
     amount = models.SmallIntegerField(default=100, blank=True, null=True)

     # ALL OF THESE WERE GENERATED BY GITHUB COPILOT:
     
     # # can be positive or negative
     # importance = models.SmallIntegerField()

     # # can be positive or negative
     # urgency = models.SmallIntegerField()

     # # can be positive or negative
     # difficulty = models.SmallIntegerField()
     
     # # can be positive or negative
     # progress = models.SmallIntegerField()


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Add more basic content blocks here
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––




class GraphBlock(ContentBlock):
     name = models.CharField(max_length=100, blank=False, null=False)
     x_label = models.CharField(max_length=100, blank=True, null=True)
     y_label = models.CharField(max_length=100, blank=True, null=True)
     data = models.JSONField(blank=True, null=True)



class CharacterWebBlock(ContentBlock):
     name = models.CharField(max_length=100, blank=False, null=False)
     # image = models.ImageField(upload_to='images/') # this was automatically created by co-pilot
     description = models.CharField(max_length=255, blank=True, null=True)

     # this was automatically created by co-pilot
     relationships = models.ManyToManyField(to='CharacterRelationship', related_name='relationships')



class TimelineBlock(ContentBlock):
     name = models.CharField(max_length=100, blank=False, null=False)
     description = models.CharField(max_length=255, blank=True, null=True)

     # this was automatically created by co-pilot
     plot_points = models.ManyToManyField(to='PlotPoint', related_name='plot_points')


# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Add more complex content blocks here
# ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––




class MapBlock(ContentBlock):
     # we took this away because "settings" already inherit the connection to the ContentBlock model (which MapBlock inherits from) through their inheritance from the Page model
     # setting = models.ForeignKey(to='Setting', on_delete=models.SET_NULL, default=None, null=True)

     name = models.CharField(max_length=100, blank=False, null=False)
     image = models.ImageField(upload_to='images/', blank=False, null=False)


class Pin(models.Model):
     map = models.ForeignKey(to='MapBlock', on_delete=models.CASCADE, blank=False, null=False)

     # Supposedly, these next three lines should allow the "name" field to come from the "name"field of any other model in the database???
     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=False, null=False)
     object_id = models.PositiveIntegerField(blank=False, null=False)
     name = GenericForeignKey('content_type', 'object_id')

     description = models.CharField(max_length=255, blank=True, null=True)
     
     # You will need to edit this icon field to be more of an SVG choice
     icon = models.ImageField(upload_to='images/', blank=True, null=True)
     x = models.PositiveSmallIntegerField(blank=False, null=False)
     y = models.PositiveSmallIntegerField(blank=False, null=False)


class Region(models.Model):
     map = models.ForeignKey(to='MapBlock', on_delete=models.CASCADE, blank=False, null=False)
     region_type = models.ForeignKey(to='RegionType', on_delete=models.CASCADE, blank=False, null=False)

     # We want this to come from the Setting, Magic, or SocialStructure
     # name = models.ForeignKey(max_length=100)

     # Supposedly, these next three lines should allow the "name" field to come from the "name"field of any other model in the database???
     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=False, null=False)
     object_id = models.PositiveIntegerField(blank=False, null=False)
     name = GenericForeignKey('content_type', 'object_id')
     
     # From the Django GEO API. This is supposed to be a polygon field that can be drawn on the map
     shape = models.GeometryField(blank=False, null=False)


# This is supposed to be a reference table for Regions so that we can standardize and protect the data from errors
class RegionType(models.Model):
     region_type_name = models.CharField(max_length=100, blank=False, null=False)

     # This might throw errors and you might need to override it (this model technically already inherits the __str__ method from the ContentBlock model)
     def __str__(self):
          return self.region_type_name



