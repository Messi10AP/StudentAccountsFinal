from django.contrib import admin
from .models import UserInfo
class UserInfoAdmin(admin.ModelAdmin):
    fields = ['user', 'fname', 'lname', 'email', 'password', 'class_of']
# Register your models here.
admin.site.register(UserInfo, UserInfoAdmin)

