from django.urls import path
from . import views


urlpatterns = [

    path("posts_list/", views.blog_view, name='home_list'),
    path("post/", views.blog_category, name='about_detail'),
    path("demo/", views.demo, name='demo'),

]
