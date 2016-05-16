from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, related_name='accounts')
    balance = models.IntegerField()
    
    def __unicode__(self):
        return "{0}".format(self.name)
    
