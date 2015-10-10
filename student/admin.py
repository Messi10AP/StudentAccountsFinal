from django.contrib import admin
from .models import UserInfo
# Register your models here.
class UserAdmin(admin.ModelAdmin):
	fields = ['user', 'grade', 'class_of', 'balance',  'pub_date']
        list_display = ['user', 'grade', 'class_of', 'balance',  'pub_date']

admin.site.register(UserInfo, UserAdmin)
