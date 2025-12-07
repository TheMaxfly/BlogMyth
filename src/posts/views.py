from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

# Create your views here.

from django.views.generic import ListView
from .models import BlogPost

class BlogHome(ListView):
    model = BlogPost
    template_name = "index.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)
    

class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ["title", "content",]



class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_update.html"
    fields = ["title", "content", "published"]


class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = "post"
    template_name = "posts/blogpost_detail.html"
