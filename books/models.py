from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75, null=True, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category name={self.name}>"

# class Author(models.Model):
#     name = models.CharField(max_length=255)
#     birthdate = models.DateField(null=True, blank=True)

#     def __repr__(self):
#         return f"<Book name={self.name} author={self.author}>"


class Books(models.Model):
    title = models.CharField(max_length=100)
    # author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True) 
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    url = models.URLField(max_length=100, blank=True)
    created_at = models.DateField(null=True, editable=False, blank=True, auto_now_add=True)
    categories = models.ManyToManyField('Category',related_name="books")

    # def __str__(self):
    #     return self.name

    # def __repr__(self):
    #     return f"<Books name={self.name}>"















# def __repr__(self):
#     return f"<Book Title={self.title} author={self.author}>"

