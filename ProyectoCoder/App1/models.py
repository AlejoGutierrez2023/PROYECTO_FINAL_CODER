from django.db import models
from django.contrib.auth.models import User
import magic
from django.core.exceptions import ValidationError

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def validate_image(self):
        mime = magic.Magic(mime=True)
        if not mime.from_buffer(self.image.read()).startswith('image'):
            raise ValidationError("Archivo no es una imagen")
    

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_delete_any_blog", "Can delete any blog"),
            ("can_edit_any_blog", "Can edit any blog"),
        ]
