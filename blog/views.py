from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comment
from .forms import PostForm


class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_at__lte=timezone.now()).order_by('-published_at')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    login_url = '/login/'
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_at__isnull=True).order_by('created_at')
