from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ViewSet, ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ProductModelViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk' # default value

class ProductViewSet(ViewSet):

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(instance=item)

        return Response(serializer.data)            

    def update(self, request, pk=None):
        queryset = Product.objects.get(pk=pk)
        serializer = ProductSerializer(instance=queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)            
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST) 

    def destroy(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        product.delete()           
        return Response(status=status.HTTP_204_NO_CONTENT) 

class UpdateRetrieveDeleteProduct(GenericAPIView, 
                        UpdateModelMixin, 
                        RetrieveModelMixin,
                        DestroyModelMixin,
                        ):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk' # default value  

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CreateListProduct(GenericAPIView, 
                        ListModelMixin, 
                        CreateModelMixin, 
                        ):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ProductList(APIView):

    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class ProductDetail(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST) 

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = ProductSerializer(instance=queryset, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = self.get_object(pk)
        serializer = ProductSerializer(instance=queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)            
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()           
        return Response(status=status.HTTP_204_NO_CONTENT) 

@api_view(["GET", "POST"])
def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        #print(Product.objects.values())
        serializer = ProductSerializer(instance=products, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)            
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST) 

@api_view(["GET", "PUT", "DELETE"])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST) 

    if request.method == "GET":
        serializer = ProductSerializer(instance=product, many=False)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ProductSerializer(instance=product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)            
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == "DELETE":
        product.delete()           
        return Response(status=status.HTTP_204_NO_CONTENT) 


