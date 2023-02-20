from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# Global Permissions Choices
PERMISSIONS = (
     ('O', 'Owner'),
     ('E', 'Editor'),
     ('V', 'Viewer'),
)

# Create your models here.

# The User class inherits from the AbstractUser class from django.contrib.auth.models
class Profile(models.Model):
     # The AbstractUser model has: 

     # username: A field for the user's username. This field is required and must be unique.
     # first_name: A field for the user's first name.
     # last_name: A field for the user's last name.
     # email: A field for the user's email address. This field is required and must be unique.
     # is_staff: A boolean field that indicates whether the user is a staff member.
     # is_active: A boolean field that indicates whether the user is active.
     # date_joined: A field that stores the date and time that the user was created.
     # password: A field for storing the user's hashed password.
     # groups: A many-to-many field for storing the groups that the user is a member of.
     # user_permissions: A many-to-many field for storing the permissions that are granted to the user.
     # last_login: A field that stores the date and time of the user's last login.
     # is_superuser: A boolean field that indicates whether the user is a superuser.
     # get_full_name(): A method that returns the user's full name.
     # get_short_name(): A method that returns the user's first name.
     # __str__(): A method that returns a string representation of the user.
     user = models.OneToOneField(to=User, on_delete=models.CASCADE)
     birthday = models.DateField(auto_now=False, auto_now_add=False)
     primary_content_type = models.CharField(max_length=50)
     description = models.CharField(max_length=255)
     date_first_published = models.DateTimeField(auto_now_add=False)
     theme = models.ForeignKey(to='Theme', on_delete=models.SET_NULL, null=True)
     media_projects = models.ManyToManyField(to='wiki.MediaProject')
     realms = models.ManyToManyField(to='worldbuilding.Realm', through='UserRealmsAccess')
     
     
class UserRealmsAccess(models.Model):

     user = models.ForeignKey(to='Profile', on_delete=models.CASCADE)
     realm = models.ForeignKey(to='worldbuilding.Realm', on_delete=models.CASCADE)
     permissions = models.CharField(max_length=1, choices=PERMISSIONS, default='V')
     

     def __str__(self):
          return self.user.username + ' - ' + self.realm.name + ' realm - ' + self.access_level
     
     
class UserPageAccess(models.Model):

     user = models.ForeignKey(to='Profile', on_delete=models.CASCADE)
     page = models.ForeignKey(to='worldbuilding.Page', on_delete=models.CASCADE)
     access_level = models.CharField(max_length=1, choices=PERMISSIONS, default='V')
     

     def __str__(self):
          return self.user.username + ' - ' + self.page.name + ' page - ' + self.access_level


class UserMediaProjectAccess(models.Model):
     user = models.ForeignKey(to='Profile', on_delete=models.CASCADE)
     media_project = models.ForeignKey(to='wiki.MediaProject', on_delete=models.CASCADE)
     
     access_level = models.CharField(max_length=1, choices=PERMISSIONS, default='V')     

     def __str__(self):
          return self.user.username + ' - ' + self.media_project.name + ' media project - ' + self.access_level


class Theme(models.Model):
     name = models.CharField(max_length=50)
     # description = models.CharField(max_length=255)
     primary_color = models.CharField(max_length=7)
     secondary_color = models.CharField(max_length=7)
     tertiary_color = models.CharField(max_length=7)
     button_style = models.CharField(max_length=10)
     corner_roundness = models.PositiveSmallIntegerField()
     background_blur_amount = models.PositiveSmallIntegerField()

     def __str__(self):
          return self.name

