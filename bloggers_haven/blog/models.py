from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:20]}"
    
    

    ,