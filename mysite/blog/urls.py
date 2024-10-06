from django.urls import path
from .views import PostList, PostDetail  # Import your views

app_name = 'blog'

urlpatterns = [
    # Post views
    path('', PostList.as_view(), name='post_list'),  # Use PostList.as_view() for class-based view
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
        PostDetail.as_view(),  # Use PostDetail.as_view() for class-based view
        name='post_detail'
    ),
]
