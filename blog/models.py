from django.conf import settings
from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    """To post the article of the blog."""

    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    category = models.CharField(max_length=50)
    tags = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title
