from django.db import models
#from markdownx.models import MarkdownxField


class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
        


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    part1 = models.TextField(default="Contenu")
    part2 = models.TextField(default="Contenu")
    part3 = models.TextField(default="Contenu")
    part4 = models.TextField(default="Contenu")
    part5 = models.TextField(default="Contenu")
    part6 = models.TextField(default="Contenu")
    part7 = models.TextField(default="Contenu")
    part8 = models.TextField(default="Contenu")
    part9 = models.TextField(default="Contenu")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name= 'posts')



    def __str__(self) :
        return self.title
    


