from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Config)
admin.site.register(Role)
admin.site.register(Acl)
admin.site.register(Devices)
admin.site.register(Users)
admin.site.register(Usergroups)
admin.site.register(Usergroupmember)
admin.site.register(Usergroupdevices)
admin.site.register(Frusers)
admin.site.register(Frusergroups)
admin.site.register(Frusergroupmember)
admin.site.register(Frusergroupdevices)
admin.site.register(Fruserlogs)
admin.site.register(Systemlogs)
