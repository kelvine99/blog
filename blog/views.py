from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView	
from django.views.generic.edit import CreateView

from.models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

def blogs(request):
    context ={
        "blogs":Post.objects.all(),
    }
    return render(request, "home.html", context)
    # context_object_name = "blogs"

class BlogDetailView(DetailView):
    model = Post
    template_name= 'post_detail.html'

class BlogCreateView(CreateView):
    model=Post
    template_name='post_edit_new.html'
    fields=['title','author','body']

class BlogUpdateView(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title','body']


# Create your views here.class 
class BlogDeleteView(DeleteView):
    model = Post
    templete_name = 'postdelete.html'
    success_url = reverse_lazy('home')
