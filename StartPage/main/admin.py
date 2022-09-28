from django.contrib import admin
from .models import NewsSite, FavSite, Settings

# Register your models here.
admin.site.register(NewsSite)
admin.site.register(FavSite)
admin.site.register(Settings)
