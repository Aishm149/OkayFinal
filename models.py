from django.core.urlresolvers import reverse

# Create your models here.
from django.db import models
class Post(models.Model):
    lockerId = models.ForeignKey('auth.User')
    lockerName = models.CharField(max_length=20)
    prime = models.IntegerField()
    standard = models.IntegerField()




