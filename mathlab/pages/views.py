from django.views import generic

from django.db import models
from .models import Post


class AboutView(generic.TemplateView):
    template_name = "home/about.html"


class PostDetailView(generic.DetailView):
    template_name = 'home/post_detail.html'
    model = Post
    context_object_name = 'post'


class IndexView(generic.TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = {
            'posts': Post.objects.all()

        }
        return context


class ContactView(generic.TemplateView):
    template_name = "home/contact.html"
