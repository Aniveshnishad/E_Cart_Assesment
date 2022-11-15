from rest_framework import serializers
from products.models import ProductMaster, Products, StorMaster


class ProductsSerializer(serializers.ModelSerializer):
    """ Product serializer """

    class Meta:
        """ product serializer Meta class """
        model = Products
        fields = ['id', 'item_name', 'unit', 'price']


class StorMasterSerializer(serializers.ModelSerializer):
    """ stor master serializer """

    class Meta:
        """ meta class of stor master """
        model = StorMaster
        fields = ['id', 'product', 'stor_master_name', 'location']


class ProductMasterSerializer(serializers.ModelSerializer):
    """ product master serializer"""

    class Meta:
        """ meta class of stor master """
        model = StorMaster
        fields = ['id', 'product', 'stor_master_name', 'location']
