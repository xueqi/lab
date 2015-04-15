from django.db import models
from box.models import Box

# Create your models here.

class Entry(models.Model):
    uid = models.CharField(max_length = 10, unique = True)
    name = models.CharField(max_length = 255, default = "", null = False, blank = False)
    box = models.ForeignKey(Box)
    row = models.IntegerField(default = 0)
    col = models.IntegerField(default = 0)
    entry_type = models.CharField(max_length = 256, default = "DNA")
    description = models.TextField(max_length = 256, null = True, blank = True)
    
    def location_as_string(self):
        return chr(ord('A') + self.row - 1) + str(self.col)
