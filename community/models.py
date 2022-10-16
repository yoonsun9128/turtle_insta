from turtle import title
from xml.etree.ElementTree import Comment
from django.db import models
from users.models import User

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=50)
    commnet = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    edite_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)