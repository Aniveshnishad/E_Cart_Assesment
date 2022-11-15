from django.urls import path, include
from rest_framework import routers
from products.views import *

router = routers.DefaultRouter()
router.register('stor_master', StorMasterViewSet)
router.register('product_master', StorMasterViewSet)

urlpatterns = [
    path('get', GetProducts.as_view(), name="get_all_product"),
    path('get/<int:id>', GetProducts.as_view(), name="get_products"),
    path('create/', ProductAPI.as_view(), name="create_products"),
    path('update/<int:id>', ProductAPI.as_view(), name='update_products'),
    path('stor/',  include(router.urls), name='stor_master'),
    path('product/',  include(router.urls), name='product_master')
]
