from django.conf.urls import include, url

urlpatterns = [
    url(r'^(\d+)$', 'box.views.show', name = 'show'),
    url(r'^edit/(\d+)$', 'box.views.edit', name = 'edit'),
    url(r'^add$', 'box.views.add', name = 'add'),
    url(r'^delete/(\d+)$', 'box.views.delete', name = 'delete'),
    url(r'^$', 'box.views.list', name='list'),

]
