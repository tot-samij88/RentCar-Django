from django.contrib import admin

from .models import CarManager

class CarManagerAdmin(admin.ModelAdmin):
    list_display=("id","name","position","phone1","tg","email","is_published")
    list_display_links=("id","name","phone1","email")
    search_fields = ("id","name","phone1","phone2","phone3","tg","email")
    list_editable = ("is_published",)
    list_per_page = 10


admin.site.register(CarManager,CarManagerAdmin)
