from django.contrib import admin
from .models import *

# Register your models here.
from .models import City

admin.site.register(City)
admin.site.register(Region)
