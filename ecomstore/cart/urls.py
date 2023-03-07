from django.urls import path,include,re_path
from ecomstore import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    show_cart
)

urlpatterns = [
    re_path(r'^$',show_cart), 
]