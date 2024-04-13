from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
from django.db import models
from .models import Post


class PostView(TemplateView):
    template_name = 'home/index.html'
    context_object_name = 'post_list'
    render(template_name='home/index.html')

    def get_queryset(self):
        return


class PostDetailView(generic.DetailView):
    template_name = 'home/post_detail.html'
    model = Post
    context_object_name = 'post'


class DemoView(LoginRequiredMixin, generic.CreateView):
    models = Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super.object.get_absolute_url()