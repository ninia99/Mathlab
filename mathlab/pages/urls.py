from django.urls import path
from .views import IndexView, ContactView, PostDetailView, AboutView, DemoView, SourceView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("details/<int:pk>", PostDetailView.as_view(), name="detail"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("about/", AboutView.as_view(), name="about"),
    path("demo/", DemoView.as_view(), name="demo"),
    path("source/", SourceView.as_view(), name="source")
    # path("download/", DownloadView.as_view(), name="download"),
]
