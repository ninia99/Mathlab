from django.urls import path
from . import views
from .views import CategoryView, ListPostView, DetailPostView


urlpatterns = [
    path("category/<slug:slug>/", CategoryView.as_view(), name='category'),
    path("posts/", ListPostView.as_view(), name='posts'),
    path("post/<slug:slug>/", DetailPostView.as_view(), name='post'),
]
