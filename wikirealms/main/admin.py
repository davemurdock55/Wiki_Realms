from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Profile)
admin.site.register(UserRealmsAccess)
admin.site.register(UserPageAccess)
admin.site.register(UserMediaProjectAccess)
admin.site.register(Theme)

