from django.contrib import admin

from apps.cars.models import Car, SpecialMarks, PeriodsOwnership

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['license_plate','brand', 'model']
    # fields = ['brand', 'model']
    list_filter = ['license_plate', 'model', 'brand', 'year', 'color','rudder_location']
    list_per_page = 20
    search_fields = ['license_plate', 'model', 'brand', 'year', 'color','rudder_location']
    
    
@admin.register(SpecialMarks)
class SpecialMarksAdmin(admin.ModelAdmin):
    list_display = ['car', 'title']
    list_filter = ['car', 'title']
    list_per_page = 20
    search_fields = ['car__brand', 'title']

@admin.register(PeriodsOwnership)
class PeriodsOwnershipsAdmin(admin.ModelAdmin):
    list_display = ['car', 'from_date', 'before_date']
    list_filter = ['car', 'from_date', 'before_date']
    list_per_page = 20
    search_fields = ['car__brand', 'from_date', 'before_date']