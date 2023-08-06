from django.contrib import admin
from . models import *
# Register your models here.

class dateAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

# class x(admin.TabularInline):
#     model = Categories

# class y(admin.TabularInline):
#     model = Price_Type

# class xyAdmin(admin.ModelAdmin):
#     inlines = [x,y]

admin.site.register(Contact_Page,dateAdmin)
admin.site.register(Event_Details)
