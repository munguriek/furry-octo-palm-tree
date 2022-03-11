from django.views.generic import ListView, DetailView
from .models import Post

class BlogHomeView(ListView):
    model = Post 
    template_name = 'home.html'
    context_object_name = 'post'
    
class BlogDetailView(DetailView):
    model = Post 
    template_name = 'post_detail.html'
    context_object_name = 'post'