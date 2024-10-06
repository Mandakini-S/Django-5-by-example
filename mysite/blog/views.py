from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListAPIView):
    queryset = Post.published.all()  # Fetch published posts
    serializer_class = PostSerializer  # Use your serializer class

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.published.all()  # Fetch published posts
    serializer_class = PostSerializer  # Use your serializer class
    lookup_field = 'slug'  # Field to lookup
    lookup_url_kwarg = 'post'  # URL keyword argument

    def get_queryset(self):
        # Filters based on publish date and slug to return a specific post
        return super().get_queryset().filter(
            publish__year=self.kwargs['year'],
            publish__month=self.kwargs['month'],
            publish__day=self.kwargs['day']
        )
