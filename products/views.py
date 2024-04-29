from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from products.models import Product

class ProductsListView(ListView):
    model = Product


class ProductsDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductsCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'category', 'photo', 'year']
    success_url = reverse_lazy(' products:products_list')


class ProductsUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'category', 'photo', 'year']
    success_url = reverse_lazy(' products:products_list')

class ProductsDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy(' products:products_list')