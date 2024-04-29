from django.urls import path
from .views import ProductsListView, ProductsDetailView, ProductsCreateView, ProductsUpdateView, ProductsDeleteView

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('products/<int:pk>/', ProductsDetailView.as_view(), name='products_detail'),
    path('products/create/', ProductsCreateView.as_view(), name='products_create'),
    path('products/<int:pk>/update/', ProductsUpdateView.as_view(), name='products_update'),
    path('products/<int:pk>/delete/', ProductsDeleteView.as_view(), name='products_delete'),
]
