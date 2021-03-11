from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from taggit.models import Tag

from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify
from datetime import date
from django.db.models import Q

from django.contrib.auth import get_user_model


#class HomeView(ListView):
#	model = Post
	#template_name = 'home.html'
	#common_tags = Post.tags.most_common()[:4]
	#ordering = ['-post_date']
def get_or_none(classmodel, **kwargs):
    try:
        return classmodel.objects.get(**kwargs)
    except classmodel.DoesNotExist:
        return None

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')

def TaggedView(request, tags):
    # Filter posts by tag name  
    tag = get_or_none(Tag,slug=tags)
    posts = Post.objects.filter(tags=tag)

    return render(request, 'tags.html', {'tags' :tag, 'posts':posts})



def PersonalDraftView(request, user):
    today = date.today()
    posts = Post.objects.filter(Q(author=user, post_date__gt= today) | Q(author=user , draft= True))
    return render(request, 'drafts.html', {'userid' :user, 'posts':posts})


def HomeView(request):
    User = get_user_model()
    users = User.objects.all()
    today = date.today()
    posts = Post.objects.filter(post_date__lte= today, draft= False)
    return render(request, 'home.html', {'posts':posts, 'users':users})

def SearchView(request):
    # Filter posts by tag name 
    today = date.today() 
    if request.method =='GET':
	    tags= request.GET.get('search')
	    tag = get_or_none(Tag,slug=tags)
	    posts = Post.objects.filter(tags=tag, draft= False, post_date__lte= today)

    return render(request, 'search.html', {'tags' :tag, 'posts':posts})

def SearchSpView(request,user):
    # Filter posts by tag name 
    today = date.today() 
    if request.method =='GET':
        tags= request.GET.get('search')
        tag = get_or_none(Tag,slug=tags)
        posts = Post.objects.filter(author=user, tags=tag, draft= False, post_date__lte= today)

    return render(request, 'search.html', {'tags' :tag, 'posts':posts})

def PersonalBlogView(request, user):
    today = date.today()
    posts = Post.objects.filter(author=user, post_date__lte= today, draft= False)
    return render(request, 'blogs.html', {'posts':posts})

    

