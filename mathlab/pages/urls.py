from django.urls import path
from . import views
from .views import CategoryView, ListPostView, DetailPostView


urlpatterns = [
    path("category/<slug:slug>/", CategoryView.as_view(), name='category'),
    path("home/", ListPostView.as_view(), name='home'),
    path("about/<slug:slug>/", DetailPostView.as_view(), name='about'),
]
