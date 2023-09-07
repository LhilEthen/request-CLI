from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', TokenObtainPairView.as_view(), name='obtain_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', obtain_auth_token, name='obtain_token'),
    path('', views.api_home, name='api-home'),
    path('create-product/', views.CreateProduct.as_view(), name='create_product'),
    # # path('add/', views.get_data, name='add-product'),
    # path('hmm/', views.main, ),
    path('product-details/<product_id>/',views.ProductDetailView.as_view()),
    # path('create/', views.CreateProduct.as_view()),
    path('products/', views.AllProducts.as_view(), name='all_products'),
    # path('list/', views.ProductListView.as_view()),
    path('product/', views.ProductMixinView.as_view())
]