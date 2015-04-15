from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'lab.views.home', name='home'),
    url(r'^box/', include('box.urls', namespace = "box")),
    url(r'^entry/', include('entry.urls', namespace = "entry")),
    url(r'^notebook/', include('notebook.urls', namespace = "notebook")),

    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += [
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT}),
            ]
