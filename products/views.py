from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from .forms import ProductForm
from .models import Product
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from .services import get_product_from_cache


class ProductsListView(ListView):
    model = Product
    template_name = 'products/product_list.html'

    def get_queryset(self):
        return get_product_from_cache()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        for product in products:
            current_version = product.versions.filter(is_current=True).first()
            product.current_version = current_version
        context['object_list'] = products
        return context

class ProductsDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class ProductsCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.slug = slugify(instance.name)
        instance.owner = self.request.user
        instance.save()
        return super().form_valid(form)

class ProductsUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user and not self.request.user.has_perm('app_name.can_change_any_description'):
            raise PermissionDenied
        return obj

    def get_success_url(self):
        return reverse_lazy('products:products_detail', kwargs={'pk': self.object.pk})

class ProductsDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products:products_list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user and not self.request.user.has_perm('app_name.can_change_any_description'):
            raise PermissionDenied
        return obj

class HomeView(View):
    template_name = 'products/home.html'

    def get(self, request):
        return render(request, self.template_name)

class ContactView(View):
    template_name = 'products/contact.html'

    def get(self, request):
        return render(request, self.template_name)
