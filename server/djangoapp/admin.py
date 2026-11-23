from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class


# CarModelAdmin class
#class CarModelAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'name', 'description']
#
#admin.site.register(CarModel, CarModelAdmin)

# CarMakeAdmin class with CarModelInline

# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)