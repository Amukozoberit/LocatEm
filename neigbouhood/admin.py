from .models import BussinessClass, Category, Location, NeigbourHood, News, Profile
from django.contrib import admin

# Register your models here.
admin.site.register(Profile)
admin.site.register(Location)
admin.site.register(NeigbourHood)
admin.site.register(BussinessClass)
admin.site.register(Category)
admin.site.register(News)


