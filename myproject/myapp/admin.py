from django.contrib import admin
from .models import *
# Register your models here.
class generatoradmin(admin.ModelAdmin):
    list_display = ('id', 'power_model','created_at','updated_at')
admin.site.register(generator,generatoradmin)

class anchor_site1(admin.ModelAdmin):
    list_display= ('id', 'site_id', 'generator', 'township')
admin.site.register(anchor_site, anchor_site1)

class team1(admin.ModelAdmin):
    list_display = ('id', 'team_name', 'leader')
admin.site.register(team, team1)

class report_data1(admin.ModelAdmin):
    list_display = ('site', 'engineer', 'fuel_cm', 'fuel_liter', 'dg_rh', 'dg_avg_rh_day', 'grid_kwh', 'oml_load', 'atom_load','mpt_load', 'mytel_load', 'cabinet_vol', 'date')
admin.site.register(report_data,report_data1)

admin.site.register(engineer_group)