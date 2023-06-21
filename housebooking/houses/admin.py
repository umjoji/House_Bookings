from django.contrib import admin
from .models import House, HouseImages, Amenity

class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'landlord', 'display_amenities')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_pictures')

# Register your models here.
admin.site.register(HouseImages, ImageAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Amenity)