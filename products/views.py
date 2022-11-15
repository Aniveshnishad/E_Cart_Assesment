
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from products.models import Products, StorMaster, ProductMaster
from products.serializers import ProductsSerializer, StorMasterSerializer, ProductMasterSerializer


class ProductAPI(APIView):
    """Api to create get and update product detail."""
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request):
        """create product data into db."""
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product create successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        if id:
            try:
                serializer_data = ProductsSerializer(Products.objects.get(id=id), data=request.data, partial=True)
            except Exception as error:
                return {"error": error}
            print(serializer_data)
            if serializer_data.is_valid():
                serializer_data.save()
                return Response({"message": "success", "result": serializer_data.data})
            else:
                return Response({"error": "given json data not validate", "result": serializer_data.errors})
        else:
            return Response({"status": "invalid detail or attribute"})


class GetProducts(APIView):
    """To get the details of products present in the database"""
    permission_classes = (IsAuthenticated,)

    def get(self, request, id=None):
        """get product data by id.
        request param : id optional."""
        if id:
            product = Products.objects.filter(id=id)
            if not product:
                return Response({"status": "invalid product id"})
            serializer = ProductsSerializer(Products.objects.get(id=id))
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        product = Products.objects.all().order_by('created_at')
        serializer = ProductsSerializer(product, context={"request": request}, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class StorMasterViewSet(viewsets.ModelViewSet):
    """helps to perform crud operation on stor master"""
    permission_classes = (IsAuthenticated, )
    queryset = StorMaster.objects.all().order_by('id')
    serializer_class = StorMasterSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """ helps to perform crud operation on  product master"""
    permission_classes = (IsAuthenticated,)
    queryset = ProductMaster.objects.all().order_by('id')
    serializer_class = ProductMasterSerializer
