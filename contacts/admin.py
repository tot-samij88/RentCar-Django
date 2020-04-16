from django.contrib import admin

from .models import Contacts

class ContactAdmin(admin.ModelAdmin):
    display = ('id','name','cars','email','phone','contact_date')
    display_links = ('id','name','cars','email')
    search_filter = ('name','email','cars')
    pagination = 20
admin.site.register(Contacts,ContactAdmin)
