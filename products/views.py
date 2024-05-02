from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from django.utils.text import slugify


class ProductsListView(ListView):
    model = Product

    def get_queryset(self):
        # Фильтруем только опубликованные товары
        return Product.objects.filter(published=True)


class ProductsDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductsCreateView(CreateView):
    model = Product
    fields = ['name', 'year', 'price', 'category', 'photo', 'description']
    success_url = reverse_lazy('products:products_list')

    def form_valid(self, form):
        # Получаем данные из формы
        instance = form.save(commit=False)
        # Формируем slug из имени товара
        instance.slug = slugify(instance.name)
        instance.save()
        return super().form_valid(form)


class ProductsUpdateView(UpdateView):
    model = Product
    fields = ['name', 'year', 'price', 'category', 'photo', 'description']

    def get_success_url(self):
        # Возвращаем URL просмотра обновленного товара
        return reverse_lazy('products:products_detail', kwargs={'pk': self.object.pk})


class ProductsDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:products_list')
