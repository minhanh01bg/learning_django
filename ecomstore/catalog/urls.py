from django.urls import path,include,re_path
from catalog.views import *

urlpatterns = [
 re_path(r'^$', index),
 re_path(r'^category/(?P<category_slug>[-\w]+)/$',show_category),
 re_path(r'^product/(?P<product_slug>[-\w]+)/$',show_product),
]