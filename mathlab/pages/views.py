from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
from django.db import models

from .models import Post


def blog_view(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, template_name="home/home.html", context=context)


def blog_category(request, category):
    context = {
        "category": category,
        "posts": Post

    }
    return render(request, template_name="home/home.html", context=context)
