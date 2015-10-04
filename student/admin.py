from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'fname', 'lname', 'email', 'class_of', 'pub_date']
    list_display = ('username', 'fname', 'lname', 'email', 'class_of', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']   
admin.site.register(User, UserAdmin)
# Register your models here.
