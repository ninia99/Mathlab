from django.views import generic
from django.db import models
from .models import Post, Contact, Category, About, Download, Logo


class AboutView(generic.TemplateView):
    template_name = "home/about.html"

    def get_context_data(self, **kwargs):
        context = {
            'about_object': About.objects.first()
        }
        return context


class PostDetailView(generic.DetailView):
    template_name = 'home/post_detail.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = {
            'post': Post.objects.first()
        }

        return context


class IndexView(generic.TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = {
            'posts': Post.objects.all(),
            'logos': Logo.objects.all(),

        }
        return context


class ContactView(generic.TemplateView):
    template_name = "home/contact.html"

    def get_context_data(self, **kwargs):
        context = {
            'contact': Contact.objects.first()
        }
        return context


class DemoView(generic.TemplateView):
    template_name = 'home/demo.html'

    def get_context_data(self, **kwargs):
        context = {
            'hide_demo': False
        }
        return context


class DownloadView(generic.TemplateView):
    template_name = 'home/download.html'

    def get_context_data(self, **kwargs):
        context = {
            'download': Download.objects.first()
        }

        return context
