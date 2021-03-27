from django.contrib import admin
from . models import adminsdb,addpreregdb,addvisitorsdb,addrolesdb
# Register your models here.
admin.site.register(adminsdb)
admin.site.register(addpreregdb)
admin.site.register(addvisitorsdb)
admin.site.register(addrolesdb)