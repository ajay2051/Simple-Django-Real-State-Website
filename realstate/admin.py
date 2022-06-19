from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title','price', 'num_bedrooms', 'num_bathrooms', 'area', 'address')

admin.site.register(Listing, ListingAdmin)