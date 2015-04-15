from django.db import models
# Create your models here.

class {{model_name}}(models.Model):
    name = models.CharField(max_length = 255, blank = True, null = true)
    def __unicode__(self):
        return self.name
