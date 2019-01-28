from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_dispaly = ('id','name','listing','email','contact_date')
    list_dispaly_link = ('id','name')
    search_fields = ('name','email','listing')
    list_per_page = 25



admin.site.register(Contact,ContactAdmin)

