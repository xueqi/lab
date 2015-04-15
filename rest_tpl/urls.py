from django.conf.urls import include, url

urlpatterns = [
    url(r'^(\d+)$', '{{resource_name}}.views.read', name = 'read'),
    url(r'^update/(\d+)$', '{{resource_name}}.views.update', name = 'update'),
    url(r'^create$', '{{resource_name}}.views.create', name = 'create'),
    url(r'^delete/(\d+)$', '{{resource_name}}.views.delete', name = 'delete'),
    url(r'^$', '{{resource_name}}.views.list', name='list'),

]
