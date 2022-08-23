from dataclasses import field
from django.contrib import admin
from .models import CustomerUser, User, DriverUser
# Register your models here
class DriverAdmin(admin.ModelAdmin):
    pass

class CustomAdmin(admin.ModelAdmin):
    list_display = ( 'username','email', 'phone', 'first_name', 'last_name', "is_customer", "is_driver", )


admin.site.register(User, CustomAdmin)
admin.site.register(CustomerUser)
admin.site.register(DriverUser, DriverAdmin)