from django.db import models
from django.contrib.auth.models import User 

class UserInfo(models.Model):
    user = models.ForeignKey(User)
    class_of = models.IntegerField()
    pub_date = models.DateTimeField( auto_now=True )
    grade = models.IntegerField()
    def __str__(self):
	return self.user.username

# Create your models here.
