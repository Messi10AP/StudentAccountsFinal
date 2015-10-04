from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    class_of = models.IntegerField()
    pub_date = models.DateTimeField('date edited')
    def __str__(self):
	return self.username
# Create your models here.
