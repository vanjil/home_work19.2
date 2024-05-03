from django.urls import path
from .views import ProductsListView, ProductsDetailView, ProductsCreateView, ProductsUpdateView, ProductsDeleteView, \
    HomeView, ContactView

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('<int:pk>/', ProductsDetailView.as_view(), name='products_detail'),
    path('create/', ProductsCreateView.as_view(), name='products_create'),
    path('<int:pk>/update/', ProductsUpdateView.as_view(), name='products_update'),
    path('<int:pk>/delete/', ProductsDeleteView.as_view(), name='products_delete'),
    path('home/', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
]
