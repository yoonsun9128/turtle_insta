from turtle import title
from xml.etree.ElementTree import Comment
from django.db import models
from users.models import User

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True) #자동생성
    edite_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)