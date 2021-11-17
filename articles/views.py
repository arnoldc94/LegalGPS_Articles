from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, 
    UpdateView, 
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "home.html"

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"


class ArticleCreateView( LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ["title", "author", "body",  ]
    
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

class ArticleUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = "article_edit.html"
    fields = ["title", "body"]
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.is_staff or self.request.user.is_superuser and self.request.user.is_active

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user or self.request.user.is_staff or self.request.user.is_superuser and self.request.user.is_active
