from django.db import models
from core.settings.base import AUTH_USER_MODEL
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to="posts/images/", blank=True, null=True)
    video = models.FileField(upload_to="posts/videos/", blank=True, null=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    likes = models.ManyToManyField(
        AUTH_USER_MODEL,
        related_name="liked_posts",
        blank=True
    )

    def __str__(self):
        return f"{self.author.email} - {self.text[:30]}"