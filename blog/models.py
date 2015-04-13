from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=90)
    slug = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    published = models.DateTimeField()
    author = models.ForeignKey(User)
    
    def __unicode__(self):
        return unicode(self.title)