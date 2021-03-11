from django.urls import path 
#from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, TaggedView, PersonalBlogView, PersonalDraftView, SearchView, SearchSpView

urlpatterns = [
    #path('',views.home, name = "home"),
    path('', HomeView, name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = 'article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/<int:pk>/edit', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('tags/<str:tags>/',TaggedView, name = 'tags'),

    path('blogs/<str:user>/',PersonalBlogView, name = 'blogs'),
    path('drafts/<str:user>/',PersonalDraftView, name = 'drafts'),
    path('search',SearchView, name = 'search'),
    path('blogs/<str:user>/search',SearchSpView, name = 'search_sp'),


]