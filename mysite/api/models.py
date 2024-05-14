from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    categories = models.CharField(max_length=100, default='uncategorized')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
