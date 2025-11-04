from django.db import models

class Editorial(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.IntegerField(null=True, blank=True)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField(null=True, blank=True)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name='books')
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
