from django.urls import path, include
from .views import product_list, product_detail
from .views import ProductList, ProductDetail
from .views import ProductList, ProductDetail
from .views import CreateListProduct, UpdateRetrieveDeleteProduct
from .views import ProductViewSet, ProductModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('viewset', ProductViewSet, basename='viewset')
router.register('modelviewset', ProductModelViewSet, basename='modelviewset')

urlpatterns = [
    path("decorator/", product_list),
    path("decorator/<int:pk>/", product_detail),
    path("classapiview/product/", ProductList.as_view()),
    path("classapiview/detail/<int:pk>/", ProductDetail.as_view()),
    path("genericapiview/", CreateListProduct.as_view()),
    path("genericapiview/<int:pk>/", UpdateRetrieveDeleteProduct.as_view()),
    path("", include(router.urls)),

]
