from django.conf.urls import url, include
from tblog.index import IndexView, IndexDetailView, TagView, CategoryView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^tag/(?P<tag_name>[\w-]+)/$', TagView.as_view(), name='tag-index'),
    url(r'^category/(?P<category_name>[\w-]+)/$', CategoryView.as_view(), name='category-index'),
    url(r'^(?P<alias_name>[\w-]+)\.html$', IndexDetailView.as_view(), name='article-detail'),
    url(r'^tadmin/', include('mongo_admin.urls')),
    url(r'^accounts/', include('ui.accounts.urls')),
]
