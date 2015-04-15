from django.db import models
from django.conf import settings
import os


# Create your models here.

class ForumGroup(models.Model):
    name = models.CharField(max_length = 255)
    
    def __unicode__(self):
        return self.name

class ForumUser(models.Model):
    name = models.CharField(max_length = 255)
    group = models.ForeignKey(ForumGroup, related_name = "users")
    password = models.Field(max_length = 255)
    
    def __unicode__(self):
        return self.name
class Forum(models.Model):

    parent = models.ForeignKey("Forum", related_name = "sub_forums", null = True, blank = True,default = None)
    create_time = models.DateTimeField(auto_now = False, auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)
    title = models.CharField(max_length = 255, default = "", blank = True, null = True)
    description = models.TextField(blank = True, null = True, default = "")
    
    def __unicode__(self):
        return self.title


class Article(models.Model):
    reply_to = models.ForeignKey('self', related_name = "articles", null = True, blank = True,default = None)
    create_time = models.DateTimeField(auto_now = False, auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)
    title = models.CharField(max_length = 255, default = "", blank = True, null = True)
    content = models.TextField(blank = True, null = True, default = "")
    forum = models.ForeignKey(Forum, related_name = "articles")
    main_article = models.BooleanField(default = True)


class Attachment(models.Model):
    article = models.ForeignKey(Article, related_name = "attachments")
    name = models.CharField(max_length = 255)
    uid = models.CharField(max_length = 64)
    
    def attachment_type(self):
        import re
        if re.findall("(jpg|jpeg|gif|png|tiff)$", self.name, re.I):
            return "image"
        return "unknown"
    def path(self):
        m = [self.uid[i*2:i*2+2] for i in range(len(self.uid) / 2)]
        return os.path.join(settings.UPLOAD_DIR, os.sep.join(m), self.name)
    def relative_path(self):
        m = [self.uid[i*2:i*2+2] for i in range(len(self.uid) / 2)]
        return os.path.join(os.sep.join(m), self.name)

def hash_uid(s):
    '''
        hash s to 8 chars string
    '''
    import hashlib
    m = hashlib.md5()
    m.update(s.encode('utf-8'))
    return m.hexdigest()[:8]
