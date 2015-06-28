from django.contrib import admin
from dress_pool.models import SkirtType
from dress_pool.models import DressType
from dress_pool.models import Purpose
from dress_pool.models import Dress
from dress_pool.models import RentRecord
from dress_pool.models import Picture 

class DressAdmin(admin.ModelAdmin):
	list_display = ('number','skirtType','dressType')
	search_fields = ['vendor']

# Register your models here.
admin.site.register(SkirtType)
admin.site.register(DressType)
admin.site.register(Purpose)
admin.site.register(Dress, DressAdmin)
admin.site.register(RentRecord)
admin.site.register(Picture)


