from django.urls import path
from .views import BlogView

urlpatterns = [
    path('discusion/', BlogView.as_view(), name='inicioblog'),
]