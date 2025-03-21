from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's name

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)  # Book title
    publication_year = models.IntegerField()  # Year published
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)  # Relationship to Author

    def __str__(self):
        return self.title

 
