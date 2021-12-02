from django.urls import path
from django.conf.urls import url
from base.views import product_views as views


urlpatterns = [
    path('', views.get_products, name='products'),
    url(r'(?P<pk>[a-zA-Z0-9-]+)/$', views.get_product_detail, name='product_detail'),
]
