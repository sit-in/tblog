from django.conf.urls import url, include
from tblog.index import IndexView, IndexDetailView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^(?P<alias_name>[\w-]+)\.html$', IndexDetailView.as_view(), name='article-detail'),
    url(r'^admin/', include('mongo_admin.articles.urls')),
    url(r'^accounts/', include('mongo_admin.accounts.urls')),
]
