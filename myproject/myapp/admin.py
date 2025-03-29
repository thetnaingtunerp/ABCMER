from django.contrib import admin
from .models import *
# Register your models here.
class generatoradmin(admin.ModelAdmin):
    list_display = ('id', 'power_model','created_at','updated_at')
admin.site.register(generator,generatoradmin)

