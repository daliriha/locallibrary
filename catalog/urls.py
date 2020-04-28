from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = "catalog"
urlpatterns = [
    url(r'^$', views.Index.as_view(), name="index"),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),


]
