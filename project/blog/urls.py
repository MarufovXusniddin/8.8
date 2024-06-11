from django.urls import path
from .views import BlogPostAPI, BlogPostAPIDetail, CommentAPI, CommentAPIDetail, LikeAPI, LikeAPIDetail, RegisterView, LoginView

urlpatterns = [
    path('blogposts/', BlogPostAPI.as_view()),
    path('blogpost/<int:pk>/', BlogPostAPIDetail.as_view()),
    path('Comments/', CommentAPI.as_view()),
    path('comment/<int:pk>/', CommentAPIDetail.as_view()),
    path('likes/', LikeAPI.as_view()),
    path('like/<int:pk>/', LikeAPIDetail.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]