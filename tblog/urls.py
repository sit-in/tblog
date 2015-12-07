from django.conf.urls import url, include
from tblog.index import IndexView, IndexDetailView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<alias_name>[\w-]+)\.html$', IndexDetailView.as_view(), name='article-detail'),
    url(r'^tadmin/', include('mongo_admin.urls')),
    url(r'^accounts/', include('ui.accounts.urls')),
]
