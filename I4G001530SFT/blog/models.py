from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model


current_user = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(current_user, default=None, on_delete=models.CASCADE)
    created_date = models.DateTimeField("Date created")
    published_date = models.DateTimeField("Date published")
 
 
    