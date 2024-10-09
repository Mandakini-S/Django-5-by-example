from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

class PostList(generics.ListAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'post'

    def get_queryset(self):
        return super().get_queryset().filter(
            publish__year=self.kwargs['year'],
            publish__month=self.kwargs['month'],
            publish__day=self.kwargs['day']
        )

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    if request.method == 'POST':
       
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} ({cd['email']}) recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n{cd['name']}'s comments: {cd['comments']}"
            send_mail(subject, message, 'from@example.com', [cd['to']])
            return Response({"message": "Email sent successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Form is not valid"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error": "Invalid request method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
