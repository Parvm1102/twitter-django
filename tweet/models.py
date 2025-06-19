from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(default = timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to = 'tweetPhotos/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.content[:20]}"