from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', views.PostCreateView.as_view(), name='post_new'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('posts/drafts/', views.DraftListView.as_view(), name='post_drafts'),
    path('posts/<int:pk>/publish/', views.publish_post, name='publish_post'),
    path('posts/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comments/<int:pk>/approve/', views.approve_comment, name='approve_comment'),
    path('comments/<int:pk>/remove/', views.remove_comment, name='remove_comment')
]