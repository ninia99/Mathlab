from django.urls import path
from . views import IndexView, ContactView, PostDetailView


urlpatterns = [
    path("", IndexView.as_view(), name="pages"),
    path("details/<int:pk>", PostDetailView.as_view(), name="detail"),
    path("contact/", ContactView.as_view(), name="demo"),
]
