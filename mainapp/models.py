from django.db import models
from django.utils import timezone

class Video(models.Model):
    topic = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    video = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(default=timezone.now)
