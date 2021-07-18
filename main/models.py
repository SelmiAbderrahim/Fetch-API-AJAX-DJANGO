from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    image = models.ImageField()

    def __str__(self):
        return self.fullname
    
class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]

    class Meta:
        ordering = ["-date",]