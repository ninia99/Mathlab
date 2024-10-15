from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.db import models
from .models import Post, Contact, Abouts, Logo, Source
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import ContactForm


class AboutView(generic.TemplateView):
    template_name = "home/about.html"

    def get_context_data(self, **kwargs):
        context = {

            'abouts': Abouts.objects.order_by('position')
        }
        return context


class PostDetailView(generic.DetailView):
    template_name = 'home/post_detail.html'
    model = Post
    context_object_name = 'post'


class IndexView(generic.TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = {
            'posts': Post.objects.all().order_by('position'),
            'logos': Logo.objects.all(),

        }
        return context


class ContactView(generic.TemplateView):
    template_name = "home/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = Contact.objects.first()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                send_mail(
                    'support',
                    form.cleaned_data['message'],
                    from_email='ninoshvelidze99@gmail.com',
                    recipient_list=['ninoshvelidze78@gmail.com'],

                )
                messages.success(request, 'Thank you for your messages')

            except:
                messages.error(request, 'somthing went wrong')
            return HttpResponseRedirect(reverse_lazy("contact"))
        context['form'] = form
        return self.render_to_response(context=context, **kwargs)


class DemoView(generic.TemplateView):
    template_name = 'home/demo.html'

    def get_context_data(self, **kwargs):
        context = {
            'hide_demo': True
        }
        return context


class DownloadView(generic.TemplateView):
    template_name = 'home/download.html'

    def get_context_data(self, **kwargs):
        context = {
            'download': Download.objects.first()
        }

        return context


class SourceView(generic.TemplateView):
    template_name = 'home/source.html'

    def get_context_data(self, **kwargs):
        context = {
            'source_object': Source.objects.order_by('position')
        }
        return context

