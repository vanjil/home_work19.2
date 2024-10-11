from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from rest_framework import viewsets

from .forms import AnnouncementForm
from .models import Announcement, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from .serializers import AnnouncementSerializer, CategorySerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView


@method_decorator(login_required, name='dispatch')
class AnnouncementsListView(ListView):
    model = Announcement
    template_name = 'products/announcement_list.html'

    def get_queryset(self):
        return Announcement.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        announcements = self.get_queryset()
        context['object_list'] = announcements
        return context


class AnnouncementDetailView(DetailView):
    model = Announcement

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1  # Увеличение счетчика просмотров
        self.object.save()
        return self.object


class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    form_class = AnnouncementForm
    success_url = reverse_lazy('products:announcements_list')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        return super().form_valid(form)


class AnnouncementUpdateView(LoginRequiredMixin, UpdateView):
    model = Announcement
    form_class = AnnouncementForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user and not self.request.user.has_perm('app_name.can_change_any_description'):
            raise PermissionDenied
        return obj

    def get_success_url(self):
        return reverse_lazy('products:announcement_detail', kwargs={'pk': self.object.pk})


class AnnouncementDeleteView(LoginRequiredMixin, DeleteView):
    model = Announcement
    success_url = '/announcements/'  # URL для перенаправления после удаления

    def get_object(self, queryset=None):
        announcement = super().get_object(queryset)
        if announcement.owner != self.request.user:
            raise PermissionDenied("У вас нет прав для удаления этого объявления.")
        return announcement


class HomeView(View):
    template_name = 'products/home.html'

    def get(self, request):
        return render(request, self.template_name)


class ContactView(View):
    template_name = 'products/contact.html'

    def get(self, request):
        return render(request, self.template_name)


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
