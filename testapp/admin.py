from django.contrib import admin
from testapp.models import *
# Register your models here.
class firadmin(admin.ModelAdmin):
    list_display=['subject','fir']
class prisoneradmin(admin.ModelAdmin):
    list_display=['name','address','prisoner_aadhar_no','crime','punishment','image']
class visitoradmin(admin.ModelAdmin):
    list_display=['name','visitor_aadhar_no','prisoner_aadhar_no','date_of_visit','image']
class allvisitoradmin(admin.ModelAdmin):
    list_display=['name','visitor_aadhar_no','prisoner_aadhar_no','date_of_visit','image']
class guardadmin(admin.ModelAdmin):
    list_display=['name','address','duty_hours','guard_aadhar_no','alloted_to','shift']
admin.site.register(fir,firadmin)
admin.site.register(prisoner,prisoneradmin)
admin.site.register(visitor,visitoradmin)
admin.site.register(allvisitors,allvisitoradmin)
admin.site.register(guard,guardadmin)
