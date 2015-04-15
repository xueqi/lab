from django.db import models
# Create your models here.

class Box(models.Model):
    uid = models.CharField(max_length = 10, unique = True)
    location = models.CharField(max_length = 256, default = "-20")
    description = models.TextField(blank = True, null = True)
    rows = models.IntegerField(default = 9)
    cols = models.IntegerField(default = 9)
    def __unicode__(self):
        return "%s in %s" % (self.uid, self.location)
