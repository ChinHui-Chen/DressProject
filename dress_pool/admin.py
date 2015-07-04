from django.contrib import admin
from dress_pool.models import SkirtType
from dress_pool.models import DressType
from dress_pool.models import Purpose
from dress_pool.models import Dress
from dress_pool.models import RentRecord

class DressAdmin(admin.ModelAdmin):
	list_display = ('number','skirtType','dressType')
	search_fields = ['vendor']
	readonly_fields = ('image_tag',)
	
# Register your models here.
admin.site.register(SkirtType)
admin.site.register(DressType)
admin.site.register(Purpose)
admin.site.register(Dress, DressAdmin)
admin.site.register(RentRecord)


