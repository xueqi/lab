from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'notebook.views.index', name = 'index'),

    url(r'^article/(\d+)$', 'notebook.views.article', name = 'view_article'),
    url(r'^new_article$', 'notebook.views.new_article', name = 'new_article'),
    url(r'^list_article$', 'notebook.views.list_article', name = 'list_article'),
    url(r'^forum/(\d+)$', 'notebook.views.forum', name = 'view_forum'),
]
