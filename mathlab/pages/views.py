from django.views import generic
from django.db import models
from .models import Post, Contact, Category, About, Download, Logo
from django.core.mail import send_mail


class AboutView(generic.TemplateView):
    template_name = "home/about.html"

    def get_context_data(self, **kwargs):
        context = {
            'about': About.objects.first()
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
        context = super().get_context_data(**kwargs)
        context['context'] = Contact.objects.first()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        message = request.POST.get('message')

        context.update({
            'firs_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone,
            'country': country,
            'message': message
        })

        if not first_name:
            context.update({first_name: 'please fill that field'})
        if not last_name:
            context.update({last_name: 'please fill that field'})
        if not email:
            context.update({email: 'please fill that field'})
        if not phone:
            context.update({phone: 'please fill that field'})
        if not country:
            context.update({country: 'please fill that field'})
        if not message:
            context.update({message: 'please fill that field'})
        if first_name and last_name and email and phone and country and message:
            send_mail(
                'support',
                f'{message}',
                '',
                recipient_list=['ninoshvelidzde99@gmail.com'],
                fail_silently=False,
            )
            print(context)
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
