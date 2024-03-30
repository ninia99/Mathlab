from django.urls import path
from . views import PostView, PostDetailView, DemoView


urlpatterns = [
    path("posts/", PostView.as_view(), name="pages"),
    path("details/<int:pk>", PostDetailView.as_view(), name="detail"),
    path("demo/", DemoView.as_view(), name="demo"),
]
