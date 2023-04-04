from django import forms
from .models import Blog
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'subtitle', 'body', 'image')

    def clean_image(self):
        image = self.cleaned_data['image']
        if image:
            # Comprobar el tamaño de la imagen
            if image.size > 5 * 1024 * 1024:  # 5 MB
                raise ValidationError(_('El archivo de imagen es demasiado grande (máximo 5 MB).'))
            # Comprobar el formato de la imagen
            if not image.name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                raise ValidationError(_('El formato de la imagen no es válido (solo se permiten JPG, PNG y GIF).'))
        return image
