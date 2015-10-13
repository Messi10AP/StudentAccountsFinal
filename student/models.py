from django.db import models
from django.contrib.auth.models import User 

class UserInfo(models.Model):
    user = models.ForeignKey(User)
    class_of = models.IntegerField()
    #username = user.username
    #fname = user.first_name
    #lname = user.last_name
    #email = user.email
    #Staff = user.is_staff
    pub_date = models.DateTimeField( auto_now=True)
    grade = models.IntegerField()
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    def __unicode__(self):
        return str(self.user.username)

# Create your models here.
