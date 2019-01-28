from django.contrib import admin

from .models import Listing


# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'sqft',
                    'price', 'list_date', 'realtor')
    list_filter = ('realtor', 'sqft')
    list_editable = ('is_published',)


admin.site.register(Listing, ListingAdmin)
