from django.contrib import admin
from .models import Userlog
# Register your models here.



class UserlogAdmin(admin.ModelAdmin):
    list_display = ['user', 'ip_address', 'task']


admin.site.register(Userlog,UserlogAdmin)
