from django.urls import path 
from .views import BlogHomeView, BlogDetailView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogHomeView.as_view(), name='home'),
]