from django.contrib import admin
from notebook.models import  Forum, ForumUser, ForumGroup

# Register your models here.
admin.site.register(Forum)
admin.site.register(ForumUser)
admin.site.register(ForumGroup)
