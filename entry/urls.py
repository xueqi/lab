from django.conf.urls import include, url

urlpatterns = [
    url(r'^(\d+)$', 'entry.views.show', name = 'show'),
    url(r'^edit/(\d+)$', 'entry.views.edit', name = 'edit'),
    url(r'^add$', 'entry.views.add', name = 'add'),
    url(r'^delete/(\d+)$', 'entry.views.delete', name = 'delete'),
    url(r'^$', 'entry.views.list', name = 'list'),
    # ajax

    url(r'^get_max_row_col$', 'entry.views.get_max_row_col', name = 'get_max_row_col'),
    url(r'^get_next_row_col$', 'entry.views.get_next_row_col', name = 'get_next_row_col'),
]
