from django.db import models
from django.conf import settings
import random
# Create your models here.

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #many users can many tweets or on_delete = models.SET_NULL 
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    def __str__(self):
        return self.content
    class Meta:
        ordering = ['-id']

    def serialize(self):
        return{
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200)
        }
