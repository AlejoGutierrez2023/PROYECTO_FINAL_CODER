from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    subject = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.sender} to {self.receiver}'
    

    class Meta:
        ordering = ['-timestamp']#para que los mensajes se muestren en orden cronológico inverso (del más reciente al más antiguo).


