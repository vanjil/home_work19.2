from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.utils.text import slugify

class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        # Фильтруем только опубликованные посты
        return BlogPost.objects.filter(published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'author', 'published']
    success_url = reverse_lazy('blog:blog_post_list')

    def form_valid(self, form):
        # Получаем данные из формы
        instance = form.save(commit=False)
        # Формируем slug из заголовка поста
        instance.slug = slugify(instance.title)
        instance.save()
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'author', 'published']

    def get_success_url(self):
        # Возвращаем URL просмотра обновленного поста
        return reverse_lazy('blog:blog_post_detail', kwargs={'pk': self.object.pk})


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:blog_post_list')
