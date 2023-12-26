from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class note(models.Model):
    noteId = models.BigAutoField(primary_key=True)
    noteTitle = models.CharField(max_length=100)
    noteText = models.TextField()
    noteAuthor = models.ForeignKey(User, on_delete=models.CASCADE)
    noteCreationDate = models.DateTimeField(auto_now_add=True)
    noteModifiedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.noteTitle
    