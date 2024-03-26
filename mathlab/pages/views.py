from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Category, Post, Demo


class CategoryView(generic.TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, slug=kwargs['slug'])
        return self.render_to_response(context={
            'category': category,
            'posts_list': Post.objects.filter(category=category)
        })


class ListPostView(generic.ListView):
    template_name = 'home/home.html'
    model = Post
    context_object_name = 'posts_list'


class DetailPostView(generic.DetailView):
    template_name = 'home/about.html'
    model = Post
    context_object_name = 'post'


class DemoView(generic.DetailView):
    template_name = 'home/demo.html'
    model = Demo
    context_object_name = 'demo'
