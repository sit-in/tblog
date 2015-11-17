from django.conf.urls import url, include
from tblog.index import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^articles/', include('app.articles.urls')),
    url(r'^accounts/', include('app.accounts.urls')),
]
