from django.urls import path
from .views import PostList, PostDetail, post_share  # Import the views

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),  
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', PostDetail.as_view(), name='post_detail'),
    path('<int:post_id>/share/', post_share, name='post_share'),  # Use post_share as an API endpoint
]
