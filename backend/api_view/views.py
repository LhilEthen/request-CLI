from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404
from rest_framework import generics, mixins
from .models import product
# from django
from rest_framework import authentication
from rest_framework import permissions
from .authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
import bcrypt
from django.http import JsonResponse
from rest_framework import status
from .serializers import productSerializer
from rest_framework import generics
# Create your views here.


# @authentication_classes([authentication.SessionAuthentication])
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def api_home(request):
    # model_data = product.objects.all()
    model_data: None = get_list_or_404(product)
    ser_product = productSerializer(model_data, many=True)
    return Response(ser_product.data)


@api_view(['POST', 'GET'])
def get_data(request):
    create_product = productSerializer(data=request.data)
    if create_product.is_valid(raise_exception=True):
        create_product.save()
        print(request.data)
        return Response(create_product.data, status=status.HTTP_202_ACCEPTED)
    # return Response()

@api_view(['GET'])
def main(request):
    print(request.GET)
    get_data = request.GET['param']
    print(get_data)
    return Response(request.GET)

@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated, permissions.DjangoModelPermissions])
@api_view(['GET', 'DELETE', 'PUT'])
def product_detail_view(request):
    pk=request.GET.get('pk')
    try:        
        data = product.objects.get(product_id=pk)
        if request.method == 'GET':
            serializer=productSerializer(data, many=False)
            return Response(serializer.data)
        else:
            data = product.objects.get(pk=pk)
            data.delete() 
    except product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


class ProductDetailView(generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = product.objects.all()
    serializer_class = productSerializer
    lookup_field='product_id'
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated ,permissions.DjangoModelPermissions]

class CreateProduct(generics.CreateAPIView):
    queryset = product
    serializer_class = productSerializer

class AllProducts(generics.ListAPIView):
    queryset = product.objects.all()
    serializer_class = productSerializer
    authentication_classes = [authentication.SessionAuthentication,TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]



# class CreateProduct()
# class ProductMixinView(generics.GenericAPIView,
#                        mixins.ListModelMixin,
#                        mixins.RetrieveModelMixin):
#     queryset =product.objects.all()
#     serializer_class = productSerializer
#     lookup_field = "pk"
#     def get(self, request, *args, **kwargs):
#         return  self.list(*args,)

class ProductMixinView(generics.GenericAPIView,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.CreateModelMixin):
    queryset = product.objects.all()
    serializer_class = productSerializer
    lookup_field = 'pk'
    def get(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
    

class DeleteProduct(generics.DestroyAPIView):
    queryset = product
    serializer_class = productSerializer
    lookup_field = 'pk'

class UpdateProduct(generics.UpdateAPIView):
    queryset = product.objects.all()
    serializer_class = productSerializer
    lookup_field = 'pk'


class CreateProduct(generics.CreateAPIView):
    serializer_class = productSerializer
    queryset = product


class ProductListView(generics.ListAPIView):
    serializer_class= productSerializer
    queryset = product.objects.all()
