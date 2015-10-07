from django.db import models
from django.contrib.auth.models import User 

class UserInfo(models.Model):
    user = models.ForeignKey(User)
    fname = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 30)
    class_of = models.IntegerField()
    pub_date = models.DateTimeField( auto_now=True )
    password = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    grade = models.IntegerField()
    def __str__(self):
	return self.user
class UserData(models.Model):
    user = models.CharField(max_length = 100)
    class_of = models.IntegerField()
    pub_date = models.DateTimeField( auto_now=True )
    password = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    grade = models.IntegerField()
    def __str__(self):
        return self.user

# Create your models here.
