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
        
# A user can have and can create multiple tags

class Tags(models.Model):
    user = models.ForeignKey(User, related_name='tags')
    tag_name = models.CharField(max_length=15)
    
    def __unicode__(self):
        return "{0}".format(self.tag_name)
    
