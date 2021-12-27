from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering=('-name',)

    def __str__(self):
        return self.name
    
    

    
class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=300, default="this is a legal article", blank = False, null = False)
    views = models.IntegerField(default=0)
    
    class Meta:
        ordering=('-date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_list", args=[self.id])


