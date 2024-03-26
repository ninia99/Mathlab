from django.urls import path
from . import views
from .views import CategoryView, ListPostView, DetailPostView, DemoView


urlpatterns = [
    path("category/", CategoryView.as_view(), name='category'),
    path("home/", ListPostView.as_view(), name='home'),
    path("about/<int:pk>", DetailPostView.as_view(), name='about'),
    path("demo/<int:pk>", DemoView.as_view(), name='demo'),
]
