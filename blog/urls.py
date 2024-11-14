from django.urls import path
from .views import KurslistView,CategoryListView,home,MalimListView

urlpatterns=[
    path('',home,name='bosh'),
    path('api/uzit/admin/kurs',KurslistView.as_view(),name='kurs'),
    path('api/uzit/admin/category',CategoryListView.as_view(),name='cate'),
    path('api/uzit/admin/malim',MalimListView.as_view(),name='mal'),
]


