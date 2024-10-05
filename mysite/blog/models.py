from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
 def get_queryset(self):
  return (
super().get_queryset().filter(status=Post.Status.PUBLISHED)
 )

class Post(models.Model):
 class Status(models.TextChoices):
   DRAFT = 'DF', 'Draft'
   PUBLISHED = 'PB', 'Published'

 title = models.CharField(max_length=250) #It is translated into a VARCHAR column in the SQL database.
 slug = models.SlugField(max_length=250, 
 unique_for_date='publish')
 author = models.ForeignKey(
 settings.AUTH_USER_MODEL,
 on_delete=models.CASCADE,
 related_name='blog_posts'
 )
 body = models.TextField()
 publish = models.DateTimeField(default=timezone.now) #or publish = models.DateTimeField(db_default=Now())
 created = models.DateTimeField(auto_now_add=True)
 updated = models.DateTimeField(auto_now=True)
 status = models.CharField(
   max_length=10, 
   choices=Status.choices,
   default=Status.DRAFT)
 
def get_absolute_url(self):
   return reverse(
 'blog:post_detail',
   args=[
 self.publish.year,
 self.publish.month,
 self.publish.day,
 self.slug
   ]
   )
 
objects = models.Manager() # The default manager.
published = PublishedManager()
 
class Meta:
   ordering = ('-publish',) # telling Django to sort results by the publish field in descending order by default when we query the database.
   indexes = [
     models.Index(fields=['-publish']),
   ]
def __str__(self):
   return self.title

