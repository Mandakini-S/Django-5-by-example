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

from .forms import EmailPostForm
def post_share(request, post_id):
 # Retrieve post by id
   post = get_object_or_404(
       Post,
       id=post_id,
       status=Post.Status.PUBLISHED
    )
   if request.method == 'POST':
     # Form was submitted
       form = EmailPostForm(request.POST)
       if form.is_valid():
     # Form fields passed validation
          cd = form.cleaned_data
     # ... send email
   else:
     form = EmailPostForm()
     return render(
         request,
 'blog/post/share.html',
 {
 'post': post,
 'form': form
 }
 )