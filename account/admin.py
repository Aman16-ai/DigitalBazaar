from django.contrib import admin
from .models import UserProfile,Address
 
admin.site.register((UserProfile,Address))
