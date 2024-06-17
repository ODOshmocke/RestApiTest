from django.urls import path
from . import views


urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blog-list-create'),
    path('blogposts/<int:id>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='blog-retrieve-update-destroy')

]
